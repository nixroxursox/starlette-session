import {Link} from 'react-router-dom'
import logo from '../logo.svg';

function ProductDetail(){
    return(

        <section className="container mt-4">
            <div className="row">
                <div className="col-4">
                    <img src={logo} className="img-thumbnail" alt="..."/>
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
        </section>
    )
}

export default ProductDetail;