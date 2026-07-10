<?php
require_once __DIR__ . '/data/config.php';

session_name(SESSION_NAME);
session_start();

function is_logged_in(): bool {
    return !empty($_SESSION['admin_logged_in']);
}

function require_login(): void {
    if (!is_logged_in()) {
        header('Location: index.php');
        exit;
    }
}

function login(string $password): bool {
    if (password_verify($password, ADMIN_PASSWORD_HASH)) {
        $_SESSION['admin_logged_in'] = true;
        return true;
    }
    return false;
}

function logout(): void {
    $_SESSION = [];
    session_destroy();
}
