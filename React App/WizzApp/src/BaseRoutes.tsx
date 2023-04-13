import React from 'react';
import { Routes, Route, Navigate } from 'react-router';
import FlightPage from './pages/FlightPage';
import LandingPage from './pages/LandingPage';
import Signin from './pages/Signin';
import Signup from './pages/Signup';
import Checkout from './pages/Checkout';

const BaseRoutes: React.FC = () => {
  return (
    <Routes>
      <Route path="/" index element={<LandingPage />} />
      <Route path="/flights" element={<FlightPage />} />
      <Route path="/signin" element={<Signin />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/checkout" element={<Checkout />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
};

export default BaseRoutes;
