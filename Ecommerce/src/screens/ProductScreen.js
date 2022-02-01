import React from 'react';
import { Link, useParams } from 'react-router-dom';
import { Row, Col, ListGroup, Image, Card, Button } from 'react-bootstrap';
import Rating from '../components/Rating';
import products from '../products';
const ProductScreen = () => {
const { id } = useParams();
console.log(id)
  const prd = products.find((p) => p._id === id)
  console.log(prd)

  return <>
      <Link className='btn btn-light my-3' to='/'>
          Go Back
      </Link>
      <Row>
          <Col md = {6}>
          <Image src={prd.image} fluid/>
          </Col>
          <Col md = {3}>
              <ListGroup.Item>
                  <h3>{prd && prd.name}</h3>
              </ListGroup.Item>
          </Col>
      </Row>
  </>;
};

export default ProductScreen;
