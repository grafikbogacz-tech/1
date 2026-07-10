<?php
require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/posts.php';
require_once __DIR__ . '/generator.php';
require_login();

$id = $_GET['id'] ?? '';
if (!$id) {
    header('Location: index.php');
    exit;
}

$post = post_get($id);
if ($post) {
    post_delete($id);

    // Remove generated HTML file
    $html_file = SITE_DIR . '/' . $id . '.html';
    if (file_exists($html_file)) {
        // Sprawdź czy to plik wygenerowany przez admina (nie oryginalny)
        $content = file_get_contents($html_file);
        if (strpos($content, 'Panel Bloga') !== false || strpos($content, 'article-cta-box') !== false) {
            unlink($html_file);
        }
    }

    regenerate_blog_html(posts_load());
}

header('Location: index.php?success=Wpis+usunięty.');
exit;
