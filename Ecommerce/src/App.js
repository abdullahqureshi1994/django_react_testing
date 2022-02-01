import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Container } from "react-bootstrap";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/ProductScreen";
import LoginScreen from "./screens/LoginScreen";
import CartScreen from "./screens/CartScreen";
import RegisterScreen from "./screens/RegisterScreen";

const App = () => {
  return (
    <Router>
    <Header />
    <main className="py-3">
      <Container>     
      <Routes>
        <Route exact path='/' element={<HomeScreen/>}/>
        <Route exact path='/login' element={<LoginScreen/>}/>
        <Route exact path='/register' element={<RegisterScreen/>}/>

        <Route exact path='/cart' element={<CartScreen/>}/>
        <Route  path='/product/:id' element={<ProductScreen/>}/>
      </Routes>
      </Container>
    </main>
    <Footer />
    </Router>
  );
}

export default App;
