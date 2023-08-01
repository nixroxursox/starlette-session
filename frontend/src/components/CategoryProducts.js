import logo from '../logo.svg';
import SingleProduct from './SingleProduct';

function CategoryProducts(){
    return (
        <section className='container mt-4'>
        <h3 className='mb-4'>Smartphones and Tablets</h3>
            <div className='row mb-4'>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
                <SingleProduct title="Xiaomi"/>
            </div>
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

export default CategoryProducts;