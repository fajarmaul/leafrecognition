<!DOCTYPE html>
<!--[if lt IE 9 ]><html class="no-js oldie" lang="en"> <![endif]-->
<!--[if IE 9 ]><html class="no-js oldie ie9" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!-->
<html class="no-js" lang="en">
<!--<![endif]-->

<head>

    <!--- basic page needs
    ================================================== -->
    <meta charset="utf-8">
    <title>Pengolahan Citra Digital</title>
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- mobile specific metas
    ================================================== -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSS
    ================================================== -->
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/vendor.css">
    <link rel="stylesheet" href="css/main.css">

    <!-- script
    ================================================== -->
    <script src="js/modernizr.js"></script>
    <script src="js/pace.min.js"></script>

    <!-- favicons
    ================================================== -->
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link rel="icon" href="favicon.ico" type="image/x-icon">

</head>

<body id="top">

    <!-- home
    ================================================== -->
<!--     <section id="home" class="s-home target-section" data-parallax="scroll" data-image-src="images/hero-bg.jpg" data-natural-width=3000 data-natural-height=2000 data-position-y=center>

        <div class="overlay"></div>
        <div class="shadow-overlay"></div>

        <div class="home-content">

            <div class="row home-content__main">

                <h1>
                    Citra yang anda masukan termasuk kedalam <br>
                    Kelas 
                    <?php
					    $result = exec("py -3 web.py C:/xampp/htdocs/projekpcd");
					    echo $result;
					?>
                    .
                </h1>

              	<div class="home-content__buttons">
                    <a href="index.php" class="btn btn--stroke">
                        Kembali
                    </a>
                </div>

            </div>

        </div>

    </section> -->

    <a style="margin-top: 30px; margin-left: 30px" href="index.php" class="btn btn--stroke">
        Kembali
    </a>
    <section id='works' class="s-works">

        <div class="intro-wrap">

            <div class="row section-header has-bottom-sep light-sep" data-aos="fade-up">
                <div class="col-full">
                    <h3 class="subhead">Hasil Identifikasi</h3>
                    <h1 class="display-2 display-2--light">Citra yang anda masukan termasuk kedalam <br>
                    Kelas 
                    <?php
                        $result = exec("py -3 web.py C:/xampp/htdocs/projekpcd");
                        echo $result;
                    ?>
                    .</h1>
                </div>
            </div> <!-- end section-header -->

        </div> <!-- end intro-wrap -->
        <?php if ($result == 1) { ?>
            <div class="row works-content">
                <div class="col-full masonry-wrap">
                    <div class="masonry">
        
                        <div style="margin-left: 280px" class="masonry__brick" data-aos="fade-up">
                            <div class="item-folio">
                                    
                                <div class="item-folio__thumb">
                                    <a href="images/daun/1.jpg" class="thumb-link" title="" data-size="1050x700">
                                        <img src="images/portfolio/lady-shutterbug.jpg" 
                                             srcset="images/daun/1.jpg" alt="">
                                    </a>
                                </div>
        
                                <div class="item-folio__text">
                                    <h3 class="item-folio__title">
                                        Chinese Tallow
                                    </h3>
                                </div>
        
                                <a href="https://www.behance.net/" class="item-folio__project-link" title="Project link">
                                    <i class="icon-link"></i>
                                </a>
        
                                <div class="item-folio__caption">
                                    <p>Dikenal juga sebagai Chinese tallow, pohon ini berasal dari Asia timur, dan sering kali ditemukan di Cina timur,Taiwan, dan Jepang. Pada regional ini, lilin yang membungkus biji digunakan untuk lilin dan juga sabun,sedangkan daunnya digunakan sebagai obat herbal.Tanaman ini terkenal dengan sap dan daunnya beracun dan daun yang membusuk beracung bagi spesies lainnya.</p>
                                </div>
        
                            </div>
                        </div> <!-- end masonry__brick -->

                    </div> <!-- end masonry -->
                </div> <!-- end col-full -->
            </div> <!-- end works-content -->
        <?php } else if ($result == 2) { ?>
            <div class="row works-content">
                <div class="col-full masonry-wrap">
                    <div class="masonry">
        
                        <div style="margin-left: 280px" class="masonry__brick" data-aos="fade-up">
                            <div class="item-folio">
                                    
                                <div class="item-folio__thumb">
                                    <a href="images/daun/2.jpg" class="thumb-link" title="" data-size="1050x700">
                                        <img src="images/portfolio/lady-shutterbug.jpg" 
                                             srcset="images/daun/2.jpg" alt="">
                                    </a>
                                </div>
        
                                <div class="item-folio__text">
                                    <h3 class="item-folio__title">
                                        Euphorbia Mili
                                    </h3>
                                </div>
        
                                <a href="https://www.behance.net/" class="item-folio__project-link" title="Project link">
                                    <i class="icon-link"></i>
                                </a>
        
                                <div class="item-folio__caption">
                                    <p>Euphorbia mili merupakan tanaman yang sering ditemui pada pekarangan sebagai tanaman hias maupun pada pot pot tanaman hias. Biasa disebut sebagai mahkota duri, tanaman ini memiliki ciri khas yang sangat terlihat jelas yaitu kumpulan duri yang menyelimuti batang dari tanaman ini. Selain itu tanaman ini juga memiliki bunga yang unik, yaitu berwarna kemerahan hingga merah muda yang berbentuk spiral. Tanaman ini berasal dari pulau Madagaskar, namun dibawa oleh orang-orang eropa maupun oleh pedagang dari negara lainnya ke berbagai belahan dunia sehingga kini cukup umum ditemukan di berbagai tempat. Rata-rata tanaman ini dapat tumbuh hingga mencapai tinggi 1.8 meter.</p>
                                </div>
        
                            </div>
                        </div> <!-- end masonry__brick -->

                    </div> <!-- end masonry -->
                </div> <!-- end col-full -->
            </div> <!-- end works-content -->
        <?php } else if ($result == 3) { ?>
            <div class="row works-content">
                <div class="col-full masonry-wrap">
                    <div class="masonry">
        
                        <div style="margin-left: 280px" class="masonry__brick" data-aos="fade-up">
                            <div class="item-folio">
                                    
                                <div class="item-folio__thumb">
                                    <a href="images/daun/3.jpg" class="thumb-link" title="" data-size="1050x700">
                                        <img src="images/portfolio/lady-shutterbug.jpg" 
                                             srcset="images/daun/3.jpg" alt="">
                                    </a>
                                </div>
        
                                <div class="item-folio__text">
                                    <h3 class="item-folio__title">
                                        Excoecaria
                                    </h3>
                                </div>
        
                                <a href="https://www.behance.net/" class="item-folio__project-link" title="Project link">
                                    <i class="icon-link"></i>
                                </a>
        
                                <div class="item-folio__caption">
                                    <p>Excoecaria atau tanaman sambang darah termasuk tanaman hijau abadi dari genus Excoecaria dan suku Euphorbiaceae. Habitus tanaman ini berupa semak yang tumbuh dengan tinggi tanaman sekitar 1-2 meter. Tanaman ini berasal dari Asia Tenggara dan Cina. sebagai anggota suku Euphorbiaceae, tanaman sambang darah ini akan mengeluarkan getah pada bagian batang berkayunya jika dilukai.</p>
                                </div>
        
                            </div>
                        </div> <!-- end masonry__brick -->

                    </div> <!-- end masonry -->
                </div> <!-- end col-full -->
            </div> <!-- end works-content -->
        <?php } else if ($result == 4) { ?>
            <div class="row works-content">
                <div class="col-full masonry-wrap">
                    <div class="masonry">
        
                        <div style="margin-left: 280px" class="masonry__brick" data-aos="fade-up">
                            <div class="item-folio">
                                    
                                <div class="item-folio__thumb">
                                    <a href="images/daun/4.jpg" class="thumb-link" title="" data-size="1050x700">
                                        <img src="images/portfolio/lady-shutterbug.jpg" 
                                             srcset="images/daun/4.jpg" alt="">
                                    </a>
                                </div>
        
                                <div class="item-folio__text">
                                    <h3 class="item-folio__title">
                                        Garden Croton
                                    </h3>
                                </div>
        
                                <a href="https://www.behance.net/" class="item-folio__project-link" title="Project link">
                                    <i class="icon-link"></i>
                                </a>
        
                                <div class="item-folio__caption">
                                    <p>Codiaeum variegatum, atau biasa lebih dikenal sebagai garden croton, adalah jenis tanaman yang sering dipelihara sebagai tanaman hias di berbagai tempat. Tanaman ini berasal dari benua asia, dan merupakan tanaman yang asli dari Indonesia, Malaysia, Australia, dan beberapa negara di kepulauan pasifik. Tanaman ini memiliki ciri khas yang cukup mencolok yaitu warna daunnya yang kemerahan ketika sudah matang daunnya. Tanaman ini tumbuh bersemak-semak dengan tinggi rata-rata ketika sudah dewasa sekitar 3 meter.</p>
                                </div>
        
                            </div>
                        </div> <!-- end masonry__brick -->

                    </div> <!-- end masonry -->
                </div> <!-- end col-full -->
            </div> <!-- end works-content -->
        <?php }  else if ($result == 5) { ?>
            <div class="row works-content">
                <div class="col-full masonry-wrap">
                    <div class="masonry">
        
                        <div style="margin-left: 280px" class="masonry__brick" data-aos="fade-up">
                            <div class="item-folio">
                                    
                                <div class="item-folio__thumb">
                                    <a href="images/daun/5.jpg" class="thumb-link" title="" data-size="1050x700">
                                        <img src="images/portfolio/lady-shutterbug.jpg" 
                                             srcset="images/daun/5.jpg" alt="">
                                    </a>
                                </div>
        
                                <div class="item-folio__text">
                                    <h3 class="item-folio__title">
                                        Hevea Brasiliensis
                                    </h3>
                                </div>
        
                                <a href="https://www.behance.net/" class="item-folio__project-link" title="Project link">
                                    <i class="icon-link"></i>
                                </a>
        
                                <div class="item-folio__caption">
                                    <p>Tanaman karet merupakan komoditas perkebunan yang penting dalam industri otomotif. Karet (Hevea brasiliensis) berasal dari benua Amerika dan saat ini menyebar luas ke seluruh dunia. Karet dikenal di Indonesia sejak masa kolonial Belanda, dan merupakan salah satu komoditas perkebunan yang memberikan sumbangan besar bagi perekonomian Indonesia. Diperkirakan ada lebih dari 3,4 juta hektare perkebunan karet di Indonesia, 85% di antaranya (2,9 juta hektare) merupakan perkebunan karet yang dikelola oleh rakyat atau petani skala kecil, dan sisanya dikelola oleh perkebunan besar milik negara atau swasta.</p>
                                </div>
        
                            </div>
                        </div> <!-- end masonry__brick -->

                    </div> <!-- end masonry -->
                </div> <!-- end col-full -->
            </div> <!-- end works-content -->
        <?php } ?>
    </section> <!-- end s-works -->

    <!-- photoswipe background
    ================================================== -->
    <div aria-hidden="true" class="pswp" role="dialog" tabindex="-1">

        <div class="pswp__bg"></div>
        <div class="pswp__scroll-wrap">

            <div class="pswp__container">
                <div class="pswp__item"></div>
                <div class="pswp__item"></div>
                <div class="pswp__item"></div>
            </div>

            <div class="pswp__ui pswp__ui--hidden">
                <div class="pswp__top-bar">
                    <div class="pswp__counter"></div><button class="pswp__button pswp__button--close" title="Close (Esc)"></button> <button class="pswp__button pswp__button--share" title=
                    "Share"></button> <button class="pswp__button pswp__button--fs" title="Toggle fullscreen"></button> <button class="pswp__button pswp__button--zoom" title=
                    "Zoom in/out"></button>
                    <div class="pswp__preloader">
                        <div class="pswp__preloader__icn">
                            <div class="pswp__preloader__cut">
                                <div class="pswp__preloader__donut"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
                    <div class="pswp__share-tooltip"></div>
                </div><button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)"></button> <button class="pswp__button pswp__button--arrow--right" title=
                "Next (arrow right)"></button>
                <div class="pswp__caption">
                    <div class="pswp__caption__center"></div>
                </div>
            </div>

        </div>

    </div> <!-- end photoSwipe background -->


    <!-- preloader
    ================================================== -->
    <div id="preloader">
        <div id="loader">
            <div class="line-scale-pulse-out">
                <div></div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    </div>


    <!-- Java Script
    ================================================== -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/plugins.js"></script>
    <script src="js/main.js"></script>

</body>

</html>