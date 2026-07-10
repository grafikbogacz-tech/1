<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/posts.php';
require_once __DIR__ . '/generator.php';
require_login();

$post = [
    'id' => '',
    'title' => '',
    'meta_desc' => '',
    'category' => 'Porady',
    'tags' => '',
    'date' => date('Y-m-d'),
    'hero_img' => '',
    'excerpt' => '',
    'content' => '',
    'read_min' => 5,
    'published' => false,
];

$edit_mode = false;
$error = '';

if (isset($_GET['id'])) {
    $existing = post_get($_GET['id']);
    if ($existing) {
        $post = $existing;
        $edit_mode = true;
    } else {
        header('Location: index.php');
        exit;
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title   = trim($_POST['title'] ?? '');
    $content = $_POST['content'] ?? '';

    if (!$title) {
        $error = 'Tytuł jest wymagany.';
    } else {
        $id = $edit_mode ? $post['id'] : post_make_id($title);

        // Handle existing ID collision for new posts
        if (!$edit_mode && post_get($id)) {
            $id .= '-' . date('ymd');
        }

        $post = [
            'id'         => $id,
            'title'      => $title,
            'meta_desc'  => trim($_POST['meta_desc'] ?? ''),
            'category'   => trim($_POST['category'] ?? 'Porady'),
            'tags'       => trim($_POST['tags'] ?? ''),
            'date'       => trim($_POST['date'] ?? date('Y-m-d')),
            'hero_img'   => trim($_POST['hero_img'] ?? ''),
            'excerpt'    => trim($_POST['excerpt'] ?? ''),
            'content'    => $content,
            'read_min'   => (int)($_POST['read_min'] ?? reading_time($content)),
            'published'  => isset($_POST['published']),
        ];

        post_upsert($post);

        // Generate HTML file if publishing
        if ($post['published']) {
            $html = generate_post_html($post);
            file_put_contents(SITE_DIR . '/' . $id . '.html', $html);
        }

        // Regenerate blog.html
        regenerate_blog_html(posts_load());

        $msg = $edit_mode ? 'Wpis+zaktualizowany.' : 'Wpis+dodany.';
        header("Location: index.php?success={$msg}");
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><?= $edit_mode ? 'Edytuj wpis' : 'Nowy wpis' ?> – Panel Bloga</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<!-- Quill editor -->
<link href="https://cdn.quilljs.com/1.3.7/quill.snow.css" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: #f4f6f9; color: #1a1a2e; }

.topbar { background: #005117; color: #fff; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; height: 56px; }
.topbar__brand { font-weight: 700; font-size: 17px; }
.topbar__right { display: flex; align-items: center; gap: 16px; font-size: 13px; }
.topbar__right a { color: #b8ddc5; text-decoration: none; }
.topbar__right a:hover { color: #fff; }

.edit-layout { display: grid; grid-template-columns: 1fr 300px; gap: 24px; padding: 28px 24px; max-width: 1200px; margin: 0 auto; }
@media (max-width: 900px) { .edit-layout { grid-template-columns: 1fr; } }

.card { background: #fff; border-radius: 12px; box-shadow: 0 1px 4px rgba(0,0,0,.06); padding: 24px; margin-bottom: 20px; }
.card h3 { font-size: 15px; font-weight: 600; margin-bottom: 18px; padding-bottom: 12px; border-bottom: 1px solid #f0f2f5; color: #333; }

.form-group { margin-bottom: 18px; }
.form-group label { display: block; font-size: 13px; font-weight: 500; margin-bottom: 6px; color: #444; }
.form-group input[type=text], .form-group input[type=date], .form-group input[type=number],
.form-group select, .form-group textarea {
    width: 100%; border: 1px solid #dde2e8; border-radius: 8px; padding: 9px 12px;
    font-size: 14px; font-family: inherit; outline: none; transition: border-color .2s; color: #1a1a2e;
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { border-color: #005117; }
.form-group textarea { resize: vertical; min-height: 80px; }
.form-group small { display: block; margin-top: 5px; color: #888; font-size: 12px; }

.quill-wrap { border: 1px solid #dde2e8; border-radius: 8px; overflow: hidden; }
.quill-wrap .ql-toolbar { border: none; border-bottom: 1px solid #dde2e8; background: #fafbfc; }
.quill-wrap .ql-container { border: none; font-size: 15px; min-height: 400px; }
.ql-editor { min-height: 400px; line-height: 1.75; }

.toggle-wrap { display: flex; align-items: center; gap: 10px; }
.toggle-wrap label { font-size: 14px; font-weight: 500; cursor: pointer; }
input[type=checkbox] { width: 18px; height: 18px; cursor: pointer; accent-color: #005117; }

.btn { display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; border-radius: 8px; font-size: 14px; font-weight: 500; cursor: pointer; text-decoration: none; border: 1px solid transparent; font-family: inherit; transition: all .15s; }
.btn-green { background: #005117; color: #fff; }
.btn-green:hover { background: #006b20; }
.btn-outline { background: transparent; border-color: #dde2e8; color: #444; }
.btn-outline:hover { background: #f4f6f9; }
.btn-full { width: 100%; justify-content: center; margin-bottom: 10px; }

.alert-error { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; font-size: 14px; }

.hero-preview { width: 100%; height: 150px; object-fit: cover; border-radius: 8px; margin-top: 8px; display: none; }
.upload-area { border: 2px dashed #dde2e8; border-radius: 8px; padding: 20px; text-align: center; cursor: pointer; transition: border-color .2s; }
.upload-area:hover { border-color: #005117; }
.upload-area input[type=file] { display: none; }
.upload-area p { font-size: 13px; color: #888; margin: 0; }
.upload-area strong { color: #005117; }

#upload-progress { display: none; margin-top: 8px; font-size: 13px; color: #666; }
</style>
</head>
<body>

<div class="topbar">
    <div class="topbar__brand"><?= $edit_mode ? 'Edytuj wpis' : 'Nowy wpis' ?></div>
    <div class="topbar__right">
        <a href="index.php">← Wróć do listy</a>
    </div>
</div>

<form method="POST" id="post-form">

<div class="edit-layout">

    <!-- LEFT COLUMN -->
    <div>
        <?php if ($error): ?><div class="alert-error"><?= htmlspecialchars($error) ?></div><?php endif; ?>

        <div class="card">
            <h3>Treść wpisu</h3>
            <div class="form-group">
                <label for="title">Tytuł wpisu *</label>
                <input type="text" id="title" name="title" value="<?= htmlspecialchars($post['title']) ?>" required placeholder="np. Jak wybrać drewno na schody?">
            </div>
            <div class="form-group">
                <label>Treść artykułu</label>
                <div class="quill-wrap">
                    <div id="quill-editor"><?= $post['content'] ?></div>
                </div>
                <input type="hidden" name="content" id="content-input">
            </div>
        </div>

        <div class="card">
            <h3>SEO i meta</h3>
            <div class="form-group">
                <label for="meta_desc">Meta description</label>
                <textarea id="meta_desc" name="meta_desc" rows="2" placeholder="Opis strony dla wyszukiwarek (max 160 znaków)"><?= htmlspecialchars($post['meta_desc']) ?></textarea>
                <small><span id="meta-count">0</span>/160 znaków</small>
            </div>
            <div class="form-group">
                <label for="excerpt">Fragment / zajawka (widoczny na liście bloga)</label>
                <textarea id="excerpt" name="excerpt" rows="2" placeholder="Krótki opis wpisu..."><?= htmlspecialchars($post['excerpt']) ?></textarea>
            </div>
        </div>
    </div>

    <!-- RIGHT COLUMN -->
    <div>
        <div class="card">
            <h3>Publikacja</h3>
            <div class="toggle-wrap" style="margin-bottom:18px;">
                <input type="checkbox" id="published" name="published" <?= !empty($post['published']) ? 'checked' : '' ?>>
                <label for="published">Opublikuj wpis</label>
            </div>
            <p style="font-size:12px; color:#888; margin-bottom:18px;">Zaznacz, aby wygenerować plik HTML i dodać wpis do bloga.</p>
            <button type="submit" class="btn btn-green btn-full">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>
                Zapisz wpis
            </button>
            <a href="index.php" class="btn btn-outline btn-full">Anuluj</a>
        </div>

        <div class="card">
            <h3>Szczegóły</h3>
            <div class="form-group">
                <label for="category">Kategoria</label>
                <select id="category" name="category">
                    <?php
                    $cats = ['Porady', 'Drewno', 'Inspiracje', 'Realizacje'];
                    foreach ($cats as $c):
                    ?>
                    <option value="<?= $c ?>" <?= $post['category'] === $c ? 'selected' : '' ?>><?= $c ?></option>
                    <?php endforeach; ?>
                </select>
            </div>
            <div class="form-group">
                <label for="date">Data publikacji</label>
                <input type="date" id="date" name="date" value="<?= htmlspecialchars($post['date']) ?>">
            </div>
            <div class="form-group">
                <label for="read_min">Czas czytania (minuty)</label>
                <input type="number" id="read_min" name="read_min" value="<?= (int)$post['read_min'] ?>" min="1" max="60">
            </div>
            <div class="form-group">
                <label for="tags">Tagi (oddzielone przecinkami)</label>
                <input type="text" id="tags" name="tags" value="<?= htmlspecialchars($post['tags']) ?>" placeholder="np. schody, dąb, drewno">
            </div>
        </div>

        <div class="card">
            <h3>Zdjęcie główne (hero)</h3>
            <div class="upload-area" id="upload-area" onclick="document.getElementById('file-input').click()">
                <input type="file" id="file-input" accept="image/*">
                <p><strong>Kliknij, aby wybrać zdjęcie</strong><br>JPG, PNG, WebP – max 5 MB</p>
            </div>
            <div id="upload-progress">Wgrywanie...</div>
            <div class="form-group" style="margin-top:12px;">
                <label for="hero_img">Lub podaj ścieżkę ręcznie</label>
                <input type="text" id="hero_img" name="hero_img" value="<?= htmlspecialchars($post['hero_img']) ?>" placeholder="img/blog/9/hero.jpg">
            </div>
            <img id="hero-preview" class="hero-preview"
                 src="<?= $post['hero_img'] ? '../' . htmlspecialchars($post['hero_img']) : '' ?>"
                 alt="Podgląd hero">
        </div>

        <?php if ($edit_mode): ?>
        <div class="card">
            <h3>Informacje</h3>
            <p style="font-size:13px; color:#666;">ID: <code style="background:#f0f2f5;padding:2px 6px;border-radius:4px;"><?= htmlspecialchars($post['id']) ?></code></p>
            <?php if (!empty($post['published'])): ?>
            <p style="font-size:13px; margin-top:8px;"><a href="../<?= htmlspecialchars($post['id']) ?>.html" target="_blank" style="color:#005117;">Otwórz opublikowany wpis ↗</a></p>
            <?php endif; ?>
        </div>
        <?php endif; ?>
    </div>

</div><!-- /edit-layout -->
</form>

<script src="https://cdn.quilljs.com/1.3.7/quill.min.js"></script>
<script>
// Quill editor
var quill = new Quill('#quill-editor', {
    theme: 'snow',
    modules: {
        toolbar: [
            [{ header: [1, 2, 3, false] }],
            ['bold', 'italic', 'underline'],
            [{ list: 'ordered' }, { list: 'bullet' }],
            ['blockquote', 'code-block'],
            ['link', 'image'],
            [{ color: [] }, { background: [] }],
            ['clean']
        ]
    },
    placeholder: 'Wpisz treść artykułu...'
});

// Sync Quill → hidden input on submit
document.getElementById('post-form').addEventListener('submit', function() {
    document.getElementById('content-input').value = quill.root.innerHTML;
});

// Meta desc counter
var metaInput = document.getElementById('meta_desc');
var metaCount = document.getElementById('meta-count');
function updateCount() { metaCount.textContent = metaInput.value.length; }
metaInput.addEventListener('input', updateCount);
updateCount();

// Hero preview
var heroInput = document.getElementById('hero_img');
var heroPreview = document.getElementById('hero-preview');
heroInput.addEventListener('input', function() {
    if (this.value) {
        heroPreview.src = '../' + this.value;
        heroPreview.style.display = 'block';
    } else {
        heroPreview.style.display = 'none';
    }
});
if (heroInput.value) heroPreview.style.display = 'block';

// File upload
document.getElementById('file-input').addEventListener('change', function() {
    var file = this.files[0];
    if (!file) return;
    if (file.size > 5 * 1024 * 1024) { alert('Plik za duży (max 5 MB)'); return; }

    var progress = document.getElementById('upload-progress');
    progress.style.display = 'block';
    progress.textContent = 'Wgrywanie...';

    var fd = new FormData();
    fd.append('image', file);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'upload.php');
    xhr.onload = function() {
        progress.style.display = 'none';
        try {
            var resp = JSON.parse(xhr.responseText);
            if (resp.success) {
                heroInput.value = resp.path;
                heroPreview.src = '../' + resp.path;
                heroPreview.style.display = 'block';
            } else {
                alert('Błąd: ' + resp.error);
            }
        } catch(e) {
            alert('Błąd wgrywania.');
        }
    };
    xhr.onerror = function() { progress.style.display = 'none'; alert('Błąd sieci.'); };
    xhr.send(fd);
});
</script>
</body>
</html>
