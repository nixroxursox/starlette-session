import logo from '../logo.svg';

function Home(){
    return (
    <main className='mt-4'>
            <div className='container'>
            {/* Banner: Carousel */}
            <div className='row'>
                <div id="carouselExampleDark" className="carousel carousel-dark slide col-12 mb-4" data-bs-ride='carousel'>
                <div className="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div className="carousel-inner">
                    <div className="carousel-item active" data-bs-interval="10000">
                    <img src='https://easypc.com.ph/cdn/shop/files/PROCESSOR_MOTHERBOARD_BUNDLE_DESKTOP.jpg?v=1689233724&width=1920' className="d-block w-100" alt="..." />
                    </div>
                    <div className="carousel-item" data-bs-interval="2000">
                    <img src='https://easypc.com.ph/cdn/shop/files/PROCESSOR_MOTHERBOARD_BUNDLE_DESKTOP.jpg?v=1689233724&width=1920' className="d-block w-100" alt="..." />
                    </div>
                    <div className="carousel-item">
                    <img src='https://easypc.com.ph/cdn/shop/files/PROCESSOR_MOTHERBOARD_BUNDLE_DESKTOP.jpg?v=1689233724&width=1920' className="d-block w-100" alt="..." />
                    </div>
                </div>
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
                </div>
                {/* End Banner: Carousel */}

                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <a href='#'><img src='https://cf.shopee.ph/file/ph-50009109-e2098e64ba89e9a9ad88414a05bb417b_xhdpi' className="card-img-top" alt="..."/></a>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <a href='#'><img src='https://cf.shopee.ph/file/ph-50009109-e2098e64ba89e9a9ad88414a05bb417b_xhdpi' className="card-img-top" alt="..."/></a>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <a href='#'><img src='https://cf.shopee.ph/file/ph-50009109-e2098e64ba89e9a9ad88414a05bb417b_xhdpi' className="card-img-top" alt="..."/></a>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <a href='#'><img src='https://cf.shopee.ph/file/ph-50009109-e2098e64ba89e9a9ad88414a05bb417b_xhdpi' className="card-img-top" alt="..."/></a>
                </div>
                </div>
                {/*Category Box End*/}
            </div>


            {/* Latest Products Section */}
            <h3 className='mb-4'>Latest Products<a href='#' className='float-end btn btn-dark mt-1'>View All Products <i className="fa-solid fa-arrow-right-long"></i></a></h3>
            <div className='row mb-4'>
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
            </div>
            {/* End Latest Products */}


            {/* Popular Categories Section */}
            <h3 className='mb-4'>Popular Categories<a href='#' className='float-end btn btn-dark mt-1'>View All Categories <i className="fa-solid fa-arrow-right-long"></i></a></h3>
            <div className='row mb-4'>
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Category title</h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Category title</h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Category title</h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Category title</h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
            </div>
            {/* End Popular Categories */}


            {/* Popular Products Section */}
            <h3 className='mb-4'>Popular Products<a href='#' className='float-end btn btn-dark mt-1'>View All Popular Products <i className="fa-solid fa-arrow-right-long"></i></a></h3>
            <div className='row mb-4'>
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
                {/*Product Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Product title</h4>
                    <h5 className="card-title text-muted">Price: ₱500</h5>
                    </div>
                    <div className='card-footer'>
                    <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                    <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                    </div>
                </div>
                </div>
                {/*Product Box End*/}
            </div>
            {/* End Popular Products */}

            {/* Popular Sellers Section */}
            <h3 className='mb-4'>Popular Sellers<a href='#' className='float-end btn btn-dark mt-1'>View All Sellers <i className="fa-solid fa-arrow-right-long"></i></a></h3>
            <div className='row mb-4'>
                {/*Seller Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Seller Name</h4>
                    </div>
                    <div className='card-footer'>
                        Categories: <a href='#'>Smartphones and Tablets</a>, <a href='#'>Electronic Accessories</a>, <a href='#'>E-readers and Tablets</a>
                    </div>
                </div>
                </div>
                {/*Seller Box End*/}
                {/*Seller Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Seller Name</h4>
                    </div>
                    <div className='card-footer'>
                    Categories: <a href='#'>Laptops and Computers</a>, <a href='#'>Gaming Consoles</a>, <a href='#'>Home Appliances</a>
                    </div>
                </div>
                </div>
                {/*Seller Box End*/}
                {/*Seller Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Seller Name</h4>
                    </div>
                    <div className='card-footer'>
                    Categories: <a href='#'>Wearable Devices</a>, <a href='#'>Electronic Components</a>, <a href='#'>Drones and Accessories</a>
                    </div>
                </div>
                </div>
                {/*Seller Box End*/}
                {/*Seller Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title">Seller Name</h4>
                    </div>
                    <div className='card-footer'>
                    Categories: <a href='#'>Cameras and Photography Gears</a>, <a href='#'>Batteries and Power Banks</a>
                    </div>
                </div>
                </div>
                {/*Seller Box End*/}
            </div>
            {/* End Popular Sellers*/}

            {/* Rating and Review s*/}
            <div id="carouselExampleIndicators" className="carousel carousel-dark slide my-4 p-5">
                <div className="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div className="carousel-inner">
                <div className="carousel-item active">
                    <figure className="text-center">
                    <blockquote className="blockquote">
                        <p>A well-known quote, contained in a blockquote element.</p>
                    </blockquote>
                    <figcaption className="blockquote-footer">
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <cite title="Source Title">Customer Name</cite>
                    </figcaption>
                    </figure>
                </div>
                <div className="carousel-item">
                    <figure className="text-center">
                    <blockquote className="blockquote">
                        <p>A well-known quote, contained in a blockquote element.</p>
                    </blockquote>
                    <figcaption className="blockquote-footer">
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <cite title="Source Title">Customer Name</cite>
                    </figcaption>
                    </figure>
                </div>
                <div className="carousel-item">
                    <figure className="text-center">
                    <blockquote className="blockquote">
                        <p>A well-known quote, contained in a blockquote element.</p>
                    </blockquote>
                    <figcaption className="blockquote-footer">
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <i className='fa fa-star text-warning'></i>
                        <cite title="Source Title">Customer Name</cite>
                    </figcaption>
                    </figure>
                </div>
                </div>
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="visually-hidden">Next</span>
                </button>
            </div>
            {/* End Rating and Reviews */}
            </div>
    </main>
    )
}

export default Home;