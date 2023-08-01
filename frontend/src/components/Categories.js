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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
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
                    <h4 className="card-title"><Link to="/">Category title</Link></h4>
                    </div>
                    <div className='card-footer'>
                        2345 Products Sold
                    </div>
                </div>
                </div>
                {/*Category Box End*/}
            </div>
            {/* End Categories */}
        </section>
    )
}

export default Categories;