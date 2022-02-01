import React from 'react';
import { Card } from 'react-bootstrap';
import Rating from './Rating';
import { Link } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
const Product = ({ product}) => {
    return (
    <Card className='my-3 p-3 rounded'>

        <Link to={`/product/${product.id}`}>
            <Card.Img
            // style={{width: 300, hieght: 200}}
            src={product.Image} variant='top' />
        </Link>

        <Card.Body>
        <Link to={`/product/${product.id}`}>
            <Card.Title as = 'div'>
                <strong>{product.Name}</strong>
            </Card.Title>
        </Link>

        <Card.Text as = 'div'>
                  <Rating value = '100'
                  text = {`$ 300 reviews`}/>
        </Card.Text>

        <Card.Text as = 'h3'>
        ${product.rate}
        </Card.Text>
        </Card.Body>
  </Card>
  )
};

export default Product;
