import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Header from './components/Header';

function App() {
  return (
    <>
    <Header/>
    <div className='desktop'>
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

          { /*Footer*/ }
          <footer className="py-5 border-top mt-5">
            <div className="row">
              <div className="col-6 col-md-2 mb-3">
                <h5>Section</h5>
                <ul className="nav flex-column">
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Home</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Features</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Pricing</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">FAQs</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">About</a></li>
                </ul>
              </div>

              <div className="col-6 col-md-2 mb-3">
                <h5>Section</h5>
                <ul className="nav flex-column">
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Home</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Features</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Pricing</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">FAQs</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">About</a></li>
                </ul>
              </div>

              <div className="col-6 col-md-2 mb-3">
                <h5>Section</h5>
                <ul className="nav flex-column">
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Home</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Features</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">Pricing</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">FAQs</a></li>
                  <li className="nav-item mb-2"><a href="#" className="nav-link p-0 text-body-secondary">About</a></li>
                </ul>
              </div>

              <div className="col-md-5 offset-md-1 mb-3">
                <form>
                  <h5>Subscribe to our newsletter</h5>
                  <p>Monthly digest of what's new and exciting from us.</p>
                  <div className="d-flex flex-column flex-sm-row w-100 gap-2">
                    <label for="newsletter1" className="visually-hidden">Email address</label>
                    <input id="newsletter1" type="text" className="form-control" placeholder="Email address"/>
                    <button className="btn btn-primary" type="button">Subscribe</button>
                  </div>
                </form>
              </div>
            </div>

            <div className="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
              <p>© 2023 Company, Inc. All rights reserved.</p>
              <ul className="list-unstyled d-flex">
                <li className="ms-3"><a className="link-body-emphasis" href="#"><i className="fa-brands fa-facebook fa-2x"></i></a></li>
                <li className="ms-3"><a className="link-body-emphasis" href="#"><i className="fa-brands fa-instagram fa-2x"></i></a></li>
                <li className="ms-3"><a className="link-body-emphasis" href="#"><i className="fa-brands fa-twitter fa-2x"></i></a></li>
              </ul>
            </div>
          </footer>
          { /*End Footer*/ }
        </div>
      </main>
    </div>

    </>
  );
}

export default App;
