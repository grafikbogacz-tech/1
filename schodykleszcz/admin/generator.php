<?php
require_once __DIR__ . '/data/config.php';

function generate_post_html(array $post): string {
    $title_esc   = htmlspecialchars($post['title'], ENT_QUOTES);
    $desc_esc    = htmlspecialchars($post['meta_desc'] ?: strip_tags(substr($post['content'], 0, 160)), ENT_QUOTES);
    $slug        = $post['id'];
    $date_pl     = date_to_pl($post['date']);
    $date_iso    = $post['date'];
    $cat         = htmlspecialchars($post['category'], ENT_QUOTES);
    $hero        = htmlspecialchars($post['hero_img'] ?: 'img/service_bg.jpg', ENT_QUOTES);
    $read_min    = (int)($post['read_min'] ?? 5);
    $tags_html   = '';
    if (!empty($post['tags'])) {
        foreach (explode(',', $post['tags']) as $tag) {
            $t = trim($tag);
            if ($t) $tags_html .= '<a href="galeria.html" class="article-tag-pill">' . htmlspecialchars($t) . '</a>';
        }
    }
    $canonical   = SITE_URL . '/' . $slug . '.html';
    $og_img      = strpos($hero, 'http') === 0 ? $hero : SITE_URL . '/' . $hero;
    $content     = $post['content'];
    $year        = substr($date_iso, 0, 4);

    return <<<HTML
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8" />
<meta name="format-detection" content="telephone=no" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta property="og:type" content="article"/>
<meta property="og:title" content="{$title_esc} | Schody Kleszcz" />
<meta name="description" content="{$desc_esc}" />
<title>{$title_esc} | Schody Kleszcz</title>
    <link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="css/swiper.min.css" rel="stylesheet" type="text/css" />
    <link href="css/simplelightbox.css" rel="stylesheet" type="text/css" />
    <link href="css/jquery-ui.css" rel="stylesheet" />
    <link href="css/style.css" rel="stylesheet" type="text/css" />
    <link href="css/font-awesome.min.css" rel="stylesheet" type="text/css" />
    <link href="img/favicon.ico" rel="shortcut icon" />
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;700&family=PT+Sans:ital,wght@0,400;0,700;1,400&family=Oswald:wght@400;500;700&display=swap&subset=latin,latin-ext" rel="stylesheet">
    <script type="application/ld+json">
    [
      {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": "https://www.schody.katowice.pl/#business",
    "name": "Schody na wymiar – Łukasz Kleszcz Stolarstwo",
    "url": "https://www.schody.katowice.pl/",
    "telephone": "+48500261410",
    "email": "stolarstwostyldom@interia.pl",
    "image": "https://www.schody.katowice.pl/img/logo.png",
    "logo": "https://www.schody.katowice.pl/img/logo.png"
  },
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{$title_esc}",
    "image": "{$og_img}",
    "datePublished": "{$date_iso}",
    "dateModified": "{$date_iso}",
    "author": {"@type":"Person","name":"Łukasz Kleszcz"},
    "publisher": {"@type":"Organization","name":"Schody Łukasz Kleszcz","logo":{"@type":"ImageObject","url":"https://www.schody.katowice.pl/img/logo.png"}}
  }
    ]
    </script>
    <link rel="canonical" href="{$canonical}" />
    <meta property="og:description" content="{$desc_esc}" />
    <meta property="og:image" content="{$og_img}" />
</head>
<body>
    <div class="is-mobile"></div>
    <div id="loader-wrapper"><div class="loader"></div></div>

    <header class="header-style-2 header-main open-style">
        <div class="wide-container-fluid">
            <div class="header-inner">
                <div class="header-logo-col">
                    <a class="logo" href="index.html"><img src="img/logo.png" alt="schody na wymiar" width="120" height="120" loading="eager"></a>
                </div>
                <div class="header-right-col">
                    <div class="header-toprow">
                        <ul class="header-contact-info">
                            <li><i class="fa fa-phone"></i><a href="tel:+48500261410">+48 500 261 410</a></li>
                            <li class="hide-md"><i class="fa fa-envelope-o"></i><a href="mailto:stolarstwostyldom@interia.pl">stolarstwostyldom@interia.pl</a></li>
                            <li class="hide-md"><i class="fa fa-clock-o"></i>Pon – Pt: 8:00 – 17:00</li>
                        </ul>
                        <ul class="header-social-icons">
                            <li><a href="https://www.facebook.com/uslugistolarskiekety" target="_blank"><i class="fa fa-facebook"></i></a></li>
                            <li><a href="https://pl.pinterest.com/schodykleszczkety" target="_blank"><i class="fa fa-pinterest-p"></i></a></li>
                        </ul>
                    </div>
                    <div class="header-navrow">
                        <div class="hamburger-icon"><span></span><span></span><span></span></div>
                        <div class="hamburger-icon-2"><span></span><span></span><span></span></div>
                        <ul class="header-menu">
                            <li><a href="index.html"><span>Strona główna</span></a></li>
                            <li><a href="onas.html"><span>O firmie</span></a></li>
                            <li><a href="oferta.html"><span>Oferta</span></a></li>
                            <li><a href="galeria.html"><span>Galeria</span></a></li>
                            <li class="active"><a href="blog.html"><span>Blog</span></a></li>
                            <li><a href="kontakt.html"><span>Kontakt</span></a></li>
                            <li class="nav-wycena"><a href="wycena.html"><span>Wycena</span></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <div class="header-green-bar"></div>
    </header>

    <div class="overlay-wrapper">
        <div class="overlay-animation"></div>
        <div class="flex"><div class="flex-in">
            <div class="overlay-menu">
                <div class="container"><div class="row">
                    <div class="btn-close"><span></span><span></span></div>
                    <div class="col-md-2 col-md-offset-5">
                        <ul>
                            <li><a href="index.html"><span>Strona główna</span></a></li>
                            <li><a href="onas.html"><span>O firmie</span></a></li>
                            <li><a href="oferta.html"><span>Oferta</span></a></li>
                            <li><a href="galeria.html"><span>Galeria</span></a></li>
                            <li class="active"><a href="blog.html"><span>Blog</span></a></li>
                            <li><a href="kontakt.html"><span>Kontakt</span></a></li>
                            <li><a href="wycena.html"><span>Wycena</span></a></li>
                        </ul>
                    </div>
                </div></div>
            </div>
        </div></div>
    </div>

    <div class="overlay-wrapper height-min video">
        <div class="overlay-animation"></div>
        <div class="iframe-wrapper"></div>
        <div class="btn-close"><span></span><span></span></div>
    </div>

    <div id="content">

        <div class="article-hero">
            <img class="article-hero__img" src="{$hero}" alt="{$title_esc}" loading="eager">
            <div class="article-hero__overlay"></div>
            <div class="article-hero__content">
                <div class="container">
                    <a href="blog.html" class="article-hero__category">{$cat}</a>
                    <h1 class="article-hero__title">{$title_esc}</h1>
                    <div class="article-hero__meta">
                        <span><i class="fa fa-user"></i>Łukasz Kleszcz</span>
                        <span><i class="fa fa-calendar"></i>{$date_pl}</span>
                        <span><i class="fa fa-clock-o"></i>{$read_min} min czytania</span>
                    </div>
                </div>
            </div>
        </div>

        <section class="article-body">
            <div class="container">
                <div class="row">
                    <div class="col-md-10 col-md-offset-1 col-sm-12 col-xs-12">

                        <div class="article-meta-bar">
                            <span><i class="fa fa-folder-open"></i><a href="blog.html">{$cat}</a></span>
                            <div class="article-tags">{$tags_html}</div>
                        </div>

                        {$content}

                        <div class="article-cta-box" style="background:#f0f7f2; border:1px solid #b8ddc5; border-radius:6px; padding:28px 32px; margin:48px 0 32px; text-align:center;">
                            <h3 style="font-family:'Oswald',sans-serif; color:#005117; margin:0 0 10px;">Masz pytania? Zadzwoń lub napisz</h3>
                            <p style="margin:0 0 18px; color:#444;">Bezpłatna wycena, fachowe doradztwo i szybka realizacja na całym Śląsku.</p>
                            <a href="tel:+48500261410" class="btn btn-primary" style="margin-right:10px;">+48 500 261 410</a>
                            <a href="wycena.html" class="btn btn-default">Wypełnij formularz wyceny</a>
                        </div>

                        <div style="margin-top:32px;">
                            <a href="blog.html" style="color:#005117; text-decoration:none; font-size:14px;">
                                <i class="fa fa-arrow-left" style="margin-right:6px;"></i>Powrót do bloga
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </div><!-- /content -->

    <footer class="footer footer-dark">
        <div class="container">
            <div class="row">
                <div class="col-md-4 col-sm-6 col-xs-12">
                    <div class="footer-logo-col">
                        <a href="index.html"><img src="img/logo.png" alt="Schody Kleszcz" width="100"></a>
                        <p>Producent schodów drewnianych na wymiar. Obsługujemy cały Śląsk i Małopolskę.</p>
                    </div>
                </div>
                <div class="col-md-4 col-sm-6 col-xs-12">
                    <h4 class="footer-heading">Kontakt</h4>
                    <ul class="footer-contact">
                        <li><i class="fa fa-phone"></i><a href="tel:+48500261410">+48 500 261 410</a></li>
                        <li><i class="fa fa-envelope-o"></i><a href="mailto:stolarstwostyldom@interia.pl">stolarstwostyldom@interia.pl</a></li>
                        <li><i class="fa fa-map-marker"></i>3 Maja 42, 32-650 Kęty</li>
                    </ul>
                </div>
                <div class="col-md-4 col-sm-12 col-xs-12">
                    <h4 class="footer-heading">Menu</h4>
                    <ul class="footer-menu">
                        <li><a href="index.html">Strona główna</a></li>
                        <li><a href="oferta.html">Oferta</a></li>
                        <li><a href="galeria.html">Galeria</a></li>
                        <li><a href="blog.html">Blog</a></li>
                        <li><a href="kontakt.html">Kontakt</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; {$year} Schody Łukasz Kleszcz. Wszelkie prawa zastrzeżone.</p>
            </div>
        </div>
    </footer>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/swiper.min.js"></script>
    <script src="js/simplelightbox.min.js"></script>
    <script src="js/jquery-ui.js"></script>
    <script src="js/scripts.js"></script>

</body>
</html>
HTML;
}

function generate_blog_card(array $post): string {
    $slug    = $post['id'];
    $title   = htmlspecialchars($post['title'], ENT_QUOTES);
    $excerpt = htmlspecialchars($post['excerpt'] ?? strip_tags(substr($post['content'], 0, 200)), ENT_QUOTES);
    $cat     = htmlspecialchars($post['category'] ?? 'Blog', ENT_QUOTES);
    $catslug = strtolower(preg_replace('/\s+/', '-', $cat));
    $hero    = htmlspecialchars($post['hero_img'] ?: 'img/service_bg.jpg', ENT_QUOTES);
    $date_pl = date_to_pl($post['date']);
    $read    = (int)($post['read_min'] ?? 5);

    return <<<HTML

                    <div class="blog-grid__item" data-category="{$catslug}">
                        <div class="blog-card-v2">
                            <div class="blog-card-v2__img">
                                <img src="{$hero}" alt="{$title}" loading="lazy">
                                <span class="blog-card-v2__cat">{$cat}</span>
                            </div>
                            <div class="blog-card-v2__body">
                                <div class="blog-card-v2__meta">
                                    <span><i class="fa fa-calendar"></i>{$date_pl}</span>
                                    <span><i class="fa fa-clock-o"></i>{$read} min</span>
                                </div>
                                <h2 class="blog-card-v2__title"><a href="{$slug}.html">{$title}</a></h2>
                                <p class="blog-card-v2__excerpt">{$excerpt}</p>
                                <a href="{$slug}.html" class="blog-card-v2__read-more">Czytaj więcej <i class="fa fa-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
HTML;
}

function regenerate_blog_html(array $posts): bool {
    $blog_file = SITE_DIR . '/blog.html';
    if (!file_exists($blog_file)) return false;

    $content = file_get_contents($blog_file);
    $start_marker = '<!-- BLOG_POSTS_START -->';
    $end_marker   = '<!-- BLOG_POSTS_END -->';

    $cards = '';
    foreach ($posts as $post) {
        if (!empty($post['published'])) {
            $cards .= generate_blog_card($post);
        }
    }

    $pos_start = strpos($content, $start_marker);
    $pos_end   = strpos($content, $end_marker);

    if ($pos_start !== false && $pos_end !== false) {
        $before = substr($content, 0, $pos_start + strlen($start_marker));
        $after  = substr($content, $pos_end);
        $new_content = $before . "\n" . $cards . "\n                    " . $after;
        file_put_contents($blog_file, $new_content);
        return true;
    }
    return false;
}

function date_to_pl(string $iso): string {
    $months = ['','stycznia','lutego','marca','kwietnia','maja','czerwca',
               'lipca','sierpnia','września','października','listopada','grudnia'];
    try {
        $d = new DateTime($iso);
        return $d->format('j') . ' ' . $months[(int)$d->format('n')] . ' ' . $d->format('Y');
    } catch (Exception $e) {
        return $iso;
    }
}
