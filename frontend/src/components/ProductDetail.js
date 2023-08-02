import {Link} from 'react-router-dom'
import logo from '../logo.svg';
import SingleProduct from './SingleProduct';

function ProductDetail(){
    return(

        <section className="container mt-4">
            <div className="row">
                <div className="col-4">
                <div id="productThumbnailSlider" className="carousel carousel-dark carousel-fade slide" data-bs-ride='carousel'>
                    <div className="carousel-indicators">
                        <button type="button" data-bs-target="#productThumbnailSlider" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                        <button type="button" data-bs-target="#productThumbnailSlider" data-bs-slide-to="1" aria-label="Slide 2"></button>
                        <button type="button" data-bs-target="#productThumbnailSlider" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div className="carousel-inner">
                        <div className="carousel-item active">
                            <img src={logo} className="img-thumbnail mb-5" alt="..."/>
                        </div>
                        <div className="carousel-item">
                            <img src={logo} className="img-thumbnail mb-5" alt="..."/>
                        </div>
                        <div className="carousel-item">
                            <img src={logo} className="img-thumbnail mb-5" alt="..."/>
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#productThumbnailSlider" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#productThumbnailSlider" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
                </div>
                <div className="col-8">
                    <h3>Product Title</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
                        ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                        velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                        sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <h4 className="card-title">Price: ₱500</h4>
                        <p className='mt-3'>
                            <Link title='Demo' target='_blank' className='btn btn-dark'><i className="fa-solid fa-cart-plus"></i> Demo</Link>
                            <button title='Add to Cart' className='btn btn-dark ms-1'><i className="fa-solid fa-cart-plus"></i> Add to Cart</button>
                            <button title='Buy Now' className='btn btn-dark ms-1'><i className="fa-solid fa-bag-shopping"></i> Buy Now</button>
                            <button title='Add to Wishlist' className='btn btn-dark ms-1'><i className="fa fa-heart"></i> Wishlist</button>
                        </p>
                        <div className='producttags mt-5 '>
                            <h5 className='product-tags'>Tags</h5>
                            <p>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                <Link to="#" className='badge bg-secondary text-white me-1'>Xiaomi</Link>
                                
                            </p>
                    </div>
                </div>
            </div>
            {/* Related Products */}
            <h3 className='mt-5 mb-3'>Related Products</h3>
            <div id="relatedProductsSlider" className="carousel carousel-dark slide" data-bs-ride='carousel'>
                <div className="carousel-indicators">
                    <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-to="2" aria-label="Slide 3"></button>
                </div>
                <div className="carousel-inner">
                    <div className="carousel-item active">
                        <div className='row mb-5'>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <div className='row mb-5'>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        </div>
                    </div>
                    <div className="carousel-item">
                        <div className='row mb-5'>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        <SingleProduct title="Xiaomi"/>
                        </div>
                    </div>
                </div>
            </div>
            {/* End Related Products */}
        </section>
    )
}

export default ProductDetail;