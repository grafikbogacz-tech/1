<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/posts.php';

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['password'])) {
    if (login($_POST['password'])) {
        header('Location: index.php');
        exit;
    } else {
        $error = 'Nieprawidłowe hasło.';
    }
}

if (isset($_GET['logout'])) {
    logout();
    header('Location: index.php');
    exit;
}

if (isset($_GET['success'])) $success = htmlspecialchars($_GET['success']);

$logged_in = is_logged_in();
$posts = $logged_in ? posts_load() : [];
?>
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Panel Bloga – Schody Kleszcz</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', sans-serif; background: #f4f6f9; color: #1a1a2e; min-height: 100vh; }

/* TOPBAR */
.topbar { background: #005117; color: #fff; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; height: 56px; }
.topbar__brand { font-weight: 700; font-size: 17px; display: flex; align-items: center; gap: 10px; }
.topbar__brand svg { width: 22px; height: 22px; fill: #7dd99a; }
.topbar__right { display: flex; align-items: center; gap: 16px; font-size: 13px; }
.topbar__right a { color: #b8ddc5; text-decoration: none; }
.topbar__right a:hover { color: #fff; }

/* LOGIN */
.login-wrap { display: flex; align-items: center; justify-content: center; min-height: calc(100vh - 56px); padding: 24px; }
.login-box { background: #fff; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,.08); padding: 48px 40px; width: 100%; max-width: 380px; }
.login-box h1 { font-size: 22px; font-weight: 700; margin-bottom: 8px; color: #005117; }
.login-box p { color: #666; font-size: 14px; margin-bottom: 28px; }
.form-group { margin-bottom: 18px; }
.form-group label { display: block; font-size: 13px; font-weight: 500; margin-bottom: 6px; color: #444; }
.form-group input { width: 100%; border: 1px solid #dde2e8; border-radius: 8px; padding: 10px 14px; font-size: 15px; font-family: inherit; outline: none; transition: border-color .2s; }
.form-group input:focus { border-color: #005117; }
.btn-primary { background: #005117; color: #fff; border: none; border-radius: 8px; padding: 11px 24px; font-size: 15px; font-weight: 600; cursor: pointer; width: 100%; font-family: inherit; transition: background .2s; }
.btn-primary:hover { background: #006b20; }
.alert { padding: 10px 14px; border-radius: 8px; font-size: 14px; margin-bottom: 16px; }
.alert-error { background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; }
.alert-success { background: #dcfce7; color: #166534; border: 1px solid #86efac; }

/* DASHBOARD */
.content { padding: 32px 24px; max-width: 1100px; margin: 0 auto; }
.page-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 28px; flex-wrap: wrap; gap: 12px; }
.page-header h1 { font-size: 24px; font-weight: 700; }
.btn { display: inline-flex; align-items: center; gap: 6px; padding: 9px 18px; border-radius: 8px; font-size: 14px; font-weight: 500; cursor: pointer; text-decoration: none; border: 1px solid transparent; font-family: inherit; transition: all .15s; }
.btn-green { background: #005117; color: #fff; }
.btn-green:hover { background: #006b20; color: #fff; }
.btn-sm { padding: 5px 12px; font-size: 13px; border-radius: 6px; }
.btn-outline { background: transparent; border-color: #dde2e8; color: #444; }
.btn-outline:hover { background: #f4f6f9; color: #1a1a2e; }
.btn-red { background: #dc2626; color: #fff; }
.btn-red:hover { background: #b91c1c; }
.btn-orange { background: #ea580c; color: #fff; }
.btn-orange:hover { background: #c2410c; }

/* CARDS GRID */
.stats-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 16px; margin-bottom: 32px; }
.stat-card { background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.stat-card__value { font-size: 32px; font-weight: 700; color: #005117; }
.stat-card__label { font-size: 13px; color: #666; margin-top: 4px; }

/* TABLE */
.table-wrap { background: #fff; border-radius: 12px; box-shadow: 0 1px 4px rgba(0,0,0,.06); overflow: hidden; }
.table-header { padding: 18px 24px; border-bottom: 1px solid #f0f2f5; display: flex; align-items: center; justify-content: space-between; }
.table-header h2 { font-size: 16px; font-weight: 600; }
table { width: 100%; border-collapse: collapse; }
th { background: #f9fafb; padding: 12px 16px; text-align: left; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: .04em; color: #666; border-bottom: 1px solid #f0f2f5; }
td { padding: 14px 16px; font-size: 14px; border-bottom: 1px solid #f9fafb; vertical-align: middle; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #fafbfc; }
.badge { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 500; }
.badge-green { background: #dcfce7; color: #166534; }
.badge-gray { background: #f3f4f6; color: #6b7280; }
.badge-blue { background: #dbeafe; color: #1e40af; }
.post-title-cell { max-width: 320px; }
.post-title-cell strong { display: block; margin-bottom: 2px; }
.post-title-cell span { font-size: 12px; color: #888; }
.actions { display: flex; gap: 6px; }
.empty-state { text-align: center; padding: 60px 20px; color: #888; }
.empty-state h3 { font-size: 18px; margin-bottom: 8px; color: #444; }
.empty-state p { font-size: 14px; margin-bottom: 20px; }

@media (max-width: 640px) {
    .table-wrap { border-radius: 0; margin: 0 -24px; }
    th.hide-sm, td.hide-sm { display: none; }
}
</style>
</head>
<body>

<div class="topbar">
    <div class="topbar__brand">
        <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        Panel Bloga – Schody Kleszcz
    </div>
    <?php if ($logged_in): ?>
    <div class="topbar__right">
        <a href="../blog.html" target="_blank">← Strona publiczna</a>
        <a href="?logout=1">Wyloguj</a>
    </div>
    <?php endif; ?>
</div>

<?php if (!$logged_in): ?>
<div class="login-wrap">
    <div class="login-box">
        <h1>Panel admina</h1>
        <p>Zaloguj się, aby zarządzać wpisami blogu.</p>
        <?php if ($error): ?><div class="alert alert-error"><?= $error ?></div><?php endif; ?>
        <form method="POST">
            <div class="form-group">
                <label for="password">Hasło</label>
                <input type="password" id="password" name="password" autofocus required placeholder="••••••••">
            </div>
            <button type="submit" class="btn-primary">Zaloguj się</button>
        </form>
        <p style="margin-top:16px; font-size:12px; color:#999;">Domyślne hasło: <strong>password</strong> — zmień je w pliku data/config.php</p>
    </div>
</div>

<?php else: ?>
<div class="content">

    <?php if ($success): ?><div class="alert alert-success" style="margin-bottom:20px;"><?= $success ?></div><?php endif; ?>

    <div class="page-header">
        <h1>Wpisy blogowe</h1>
        <a href="edit.php" class="btn btn-green">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12h14"/></svg>
            Nowy wpis
        </a>
    </div>

    <?php
    $total = count($posts);
    $published = count(array_filter($posts, fn($p) => !empty($p['published'])));
    $drafts = $total - $published;
    ?>
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-card__value"><?= $total ?></div>
            <div class="stat-card__label">Wszystkie wpisy</div>
        </div>
        <div class="stat-card">
            <div class="stat-card__value"><?= $published ?></div>
            <div class="stat-card__label">Opublikowane</div>
        </div>
        <div class="stat-card">
            <div class="stat-card__value"><?= $drafts ?></div>
            <div class="stat-card__label">Szkice</div>
        </div>
    </div>

    <div class="table-wrap">
        <div class="table-header">
            <h2>Lista wpisów</h2>
        </div>
        <?php if (empty($posts)): ?>
        <div class="empty-state">
            <h3>Brak wpisów</h3>
            <p>Nie masz jeszcze żadnych wpisów na blogu.</p>
            <a href="edit.php" class="btn btn-green">Dodaj pierwszy wpis</a>
        </div>
        <?php else: ?>
        <div style="overflow-x:auto;">
        <table>
            <thead>
                <tr>
                    <th>Tytuł</th>
                    <th class="hide-sm">Kategoria</th>
                    <th class="hide-sm">Data</th>
                    <th>Status</th>
                    <th>Akcje</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($posts as $post): ?>
                <tr>
                    <td class="post-title-cell">
                        <strong><?= htmlspecialchars($post['title']) ?></strong>
                        <span><?= htmlspecialchars($post['id']) ?>.html</span>
                    </td>
                    <td class="hide-sm">
                        <span class="badge badge-blue"><?= htmlspecialchars($post['category'] ?? '—') ?></span>
                    </td>
                    <td class="hide-sm"><?= htmlspecialchars($post['date'] ?? '—') ?></td>
                    <td>
                        <?php if (!empty($post['published'])): ?>
                            <span class="badge badge-green">Opublikowany</span>
                        <?php else: ?>
                            <span class="badge badge-gray">Szkic</span>
                        <?php endif; ?>
                    </td>
                    <td>
                        <div class="actions">
                            <a href="edit.php?id=<?= urlencode($post['id']) ?>" class="btn btn-sm btn-outline">Edytuj</a>
                            <?php if (!empty($post['published'])): ?>
                            <a href="../<?= htmlspecialchars($post['id']) ?>.html" target="_blank" class="btn btn-sm btn-outline">Podgląd</a>
                            <?php endif; ?>
                            <a href="delete.php?id=<?= urlencode($post['id']) ?>" class="btn btn-sm btn-red"
                               onclick="return confirm('Czy na pewno usunąć wpis: <?= htmlspecialchars(addslashes($post['title'])) ?>?')">Usuń</a>
                        </div>
                    </td>
                </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
        </div>
        <?php endif; ?>
    </div>

</div>
<?php endif; ?>

</body>
</html>
