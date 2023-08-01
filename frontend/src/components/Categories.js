import {Routes, Route} from 'react-router-dom';
import { Link } from 'react-router-dom';
import logo from '../logo.svg';
function Categories(){
    return (
        <section className="container mt-4">
            {/* All Categories Section */}
            <h3 className='mb-4'>All Categories</h3>
            <div className='row mb-3'>
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title"><Link to="/category/smartphones&tablets/1">Smartphones & Tablets</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Laptops & Computers</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Electronic Accessories</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Gaming Consoles</Link></h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
            </div>
            <div className='row mb-3'>
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title"><Link to="/">Home Appliances</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Wearable Devices</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Drones and Accessories</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Electronic Components</Link></h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
            </div>
            <div className='row mb-3'>
                {/*Category Box */}
                <div className='col-12 col-md-3 mb-4'>
                <div className="card shadow">
                    <img src={logo} className="card-img-top" alt="..."/>
                    <div className="card-body">
                    <h4 className="card-title"><Link to="/">Cameras and Photography Gears</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Batteries and Power Banks</Link></h4>
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
                    <h4 className="card-title"><Link to="/">E-readers and Tablets</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Electronic Components</Link></h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
            </div>
            {/* End Categories */}

            {/* Pagination*/}
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    <li class="page-item">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                    </li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                    <a class="page-link" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                    </li>
                </ul>
            </nav>
            {/* End Pagination */}
        </section>
    )
}

export default Categories;