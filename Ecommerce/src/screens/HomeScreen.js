/* eslint-disable no-lone-blocks */
import React,{useEffect,useState} from 'react';
import { Row, Col } from 'react-bootstrap';
import Product from '../components/Product';
import products from '../products';
import axios from 'axios';

const HomeScreen = () => {
  const [data , setData]= useState('')


  
  useEffect(() => {

    fetchData()
     
    
  },[]);

  const fetchData = async ()=>{

    var config = {
      method: 'get',
      url: 'acconts/showProduct/',
    };
    axios(config)
    .then(function (response) {
      console.log(response);
      setData(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });

  }




    

  return (<>
<h1>Latest Products</h1>

<Row>
    {data && data.map((product) => (
        <Col key={product.id} sm={12} md={6} lg={4} xl={3}>
           <Product product = {product} />
        </Col>
    )
    )}

</Row>
  </>
  )
};

export default HomeScreen;
