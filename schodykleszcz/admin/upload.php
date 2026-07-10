<?php
require_once __DIR__ . '/auth.php';
require_login();

header('Content-Type: application/json');

if (!isset($_FILES['image'])) {
    echo json_encode(['success' => false, 'error' => 'Brak pliku.']);
    exit;
}

$file = $_FILES['image'];
$allowed_types = ['image/jpeg', 'image/png', 'image/webp', 'image/gif'];
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mime = finfo_file($finfo, $file['tmp_name']);
finfo_close($finfo);

if (!in_array($mime, $allowed_types)) {
    echo json_encode(['success' => false, 'error' => 'Niedozwolony typ pliku. Akceptowane: JPG, PNG, WebP, GIF.']);
    exit;
}

if ($file['size'] > 5 * 1024 * 1024) {
    echo json_encode(['success' => false, 'error' => 'Plik za duży (max 5 MB).']);
    exit;
}

$ext_map = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/gif' => 'gif'];
$ext = $ext_map[$mime];
$filename = uniqid('blog_', true) . '.' . $ext;
$upload_dir = __DIR__ . '/uploads/';
$dest = $upload_dir . $filename;

if (!move_uploaded_file($file['tmp_name'], $dest)) {
    echo json_encode(['success' => false, 'error' => 'Błąd zapisu pliku.']);
    exit;
}

echo json_encode(['success' => true, 'path' => 'admin/uploads/' . $filename]);
