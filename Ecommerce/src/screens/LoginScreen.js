import React, { useState, useEffect } from 'react'
import { Form, Button } from 'react-bootstrap'
import "bootstrap/dist/css/bootstrap.min.css";
import FormContainer from '../components/FormContainer'
import { Link } from 'react-router-dom';


const LoginScreen = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')



  return (
    <FormContainer>
      <><h1>Sign In</h1><Form>
      <Form.Group controlId='email'>
        <Form.Label>Email Address</Form.Label>
        <Form.Control
          type='email'
          placeholder='Enter email'
          value={email}
        ></Form.Control>
      </Form.Group>

      <Form.Group controlId='password'>
        <Form.Label>Password</Form.Label>
        <Form.Control
          type='password'
          placeholder='Enter password'
          value={password}
        ></Form.Control>
      </Form.Group>

      <Button 
      style={{marginTop:20}}
      type='submit' variant='primary'>
        Sign In
      </Button>
     <Link to={'/register'}>
      <Button 
      style={{marginTop:20 , marginLeft: 40}}
      type='submit' variant='primary'>
        Register
      </Button>
      </Link>
    </Form></>
    </FormContainer>
   
  
  )
}

export default LoginScreen
