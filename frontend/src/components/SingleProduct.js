import logo from '../logo.svg';

function SingleProduct(props){
    return(
        <div className='col-12 col-md-3 mb-4'>
            <div className="card shadow">
                <img src={logo} className="card-img-top" alt="..."/>
                <div className="card-body">
                <h4 className="card-title">{props.title}</h4>
                <h5 className="card-title text-muted">Price: ₱500</h5>
                </div>
                <div className='card-footer'>
                <button title='Add to Cart' className='btn btn-dark btn-sm'><i className="fa-solid fa-cart-plus"></i></button>
                <button title='Add to Wishlist' className='btn btn-dark btn-sm ms-1'><i className="fa fa-heart"></i></button>
                </div>
            </div>
        </div>

    )
}

export default SingleProduct;