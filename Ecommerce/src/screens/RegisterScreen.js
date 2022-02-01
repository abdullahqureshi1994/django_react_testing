import React, { useState } from 'react'
import { Form, Button ,Row, Col } from 'react-bootstrap'

import "bootstrap/dist/css/bootstrap.min.css";
import FormContainer from '../components/FormContainer';
import { Link } from 'react-router-dom';

import axios from "axios";


const RegisterScreen = ({ location, history }) => {
  const [name, setName] = useState('')
  const [firstName, setfirstName] = useState('')
  const [lastName, setlastName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')

  const [message, setMessage] = useState(null)





  const makeAPICall = async (e) => {

  const alldata = {
    "username": name,
    "password": password,
    "password2": confirmPassword,
    "email": email,
    "first_name": firstName,
    "last_name": lastName
  }



    e.preventDefault()

    console.log("helllo")
    console.log(alldata)
    // var config = {
    //   method: 'get',
    //   url: '/acconts/showProduct/',
    // };
    
    // axios(config)
    // .then(function (response) {
    //   console.log(response);
    // })
    // .catch(function (error) {
    //   console.log(error);
    // });
  }

  return (
    <FormContainer>
      <h1>Sign Up</h1>

      <Form
      onSubmit={makeAPICall}
      >
        <Form.Group style={{ marginBottom: 10 }} controlId='name'>
          <Form.Label>User Name</Form.Label>
          <Form.Control
            required={true}
            type='empty'
            placeholder='Enter name'
            value={name}
          onChange={(e) => setName(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group style={{ marginBottom: 10 }} controlId='name'>
          <Form.Label>First Name</Form.Label>
          <Form.Control
            type='name'
            placeholder='Enter First Name'
          value={firstName}
          onChange={(e) => setfirstName(e.target.value)}
          ></Form.Control>
        </Form.Group>


        <Form.Group style={{ marginBottom: 10 }} controlId='name'>
          <Form.Label>Last Name</Form.Label>
          <Form.Control
            type='name'
            placeholder='Enter Last Name'
          value={lastName}
          onChange={(e) => setlastName(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group style={{ marginBottom: 10 }} controlId='email'>
          <Form.Label>Email Address</Form.Label>
          <Form.Control
            type='email'
            placeholder='Enter email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group style={{ marginBottom: 10 }} controlId='password'>
          <Form.Label>Password</Form.Label>
          <Form.Control
            type='password'
            placeholder='Enter password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group style={{ marginBottom: 10 }} controlId='confirmPassword'>
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control
            type='password'
            placeholder='Confirm password'
            value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Button
        // onClick={makeAPICall}
          style={{ marginTop: 10, width: 200 }}
          type='submit' variant='primary'>
          Register
        </Button>
      </Form>

      <Row className='py-3'>
        <Col>
          Have an Account?{' '}
          <Link to={'/login'}>
            Login
          </Link>
        </Col>
      </Row>
    </FormContainer>
  )
}

export default RegisterScreen
