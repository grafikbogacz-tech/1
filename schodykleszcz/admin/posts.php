<?php
require_once __DIR__ . '/data/config.php';

function posts_load(): array {
    if (!file_exists(POSTS_FILE)) return [];
    $json = file_get_contents(POSTS_FILE);
    $data = json_decode($json, true);
    return is_array($data) ? $data : [];
}

function posts_save(array $posts): void {
    file_put_contents(POSTS_FILE, json_encode($posts, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
}

function post_get(string $id): ?array {
    foreach (posts_load() as $p) {
        if ($p['id'] === $id) return $p;
    }
    return null;
}

function post_upsert(array $post): void {
    $posts = posts_load();
    $found = false;
    foreach ($posts as &$p) {
        if ($p['id'] === $post['id']) {
            $p = $post;
            $found = true;
            break;
        }
    }
    unset($p);
    if (!$found) array_unshift($posts, $post);
    posts_save($posts);
}

function post_delete(string $id): void {
    $posts = array_filter(posts_load(), fn($p) => $p['id'] !== $id);
    posts_save(array_values($posts));
}

function post_make_id(string $title): string {
    $slug = strtolower($title);
    $map = ['ą'=>'a','ć'=>'c','ę'=>'e','ł'=>'l','ń'=>'n','ó'=>'o','ś'=>'s','ź'=>'z','ż'=>'z',
            'Ą'=>'a','Ć'=>'c','Ę'=>'e','Ł'=>'l','Ń'=>'n','Ó'=>'o','Ś'=>'s','Ź'=>'z','Ż'=>'z'];
    $slug = strtr($slug, $map);
    $slug = preg_replace('/[^a-z0-9]+/', '-', $slug);
    $slug = trim($slug, '-');
    return $slug ?: 'wpis-' . time();
}

function reading_time(string $html): int {
    $text = strip_tags($html);
    $words = str_word_count($text);
    return max(1, (int)round($words / 200));
}
