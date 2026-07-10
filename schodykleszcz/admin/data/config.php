<?php
// Hasło admina – zmień po pierwszym logowaniu
// Wygeneruj hash: password_hash('TwojeHaslo', PASSWORD_DEFAULT)
define('ADMIN_PASSWORD_HASH', '$2y$12$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi'); // domyślne: password
define('SITE_URL', 'https://www.schody.katowice.pl');
define('SITE_DIR', dirname(__DIR__)); // katalog główny strony
define('POSTS_FILE', __DIR__ . '/posts.json');
define('SESSION_NAME', 'blog_admin');
