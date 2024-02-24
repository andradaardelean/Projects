import React, { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router';
import LandingPage from './pages/LandingPage';
import SignIn from './pages/Signin';
import SignUp from './pages/Signup';
import DonationPage from './pages/DonationPage';
import EmployeePage from './pages/EmployeePage';
import CenterPage from './pages/CenterPage';
import Cookies from 'js-cookie';

const BaseRoutes: React.FC = () => {
  const [userType, setUserType] = useState<string | null>(Cookies.get('userType') ?? null);
  useEffect(() => {
    setUserType(Cookies.get('userType') ?? null);
  }, []);

  if (userType === '1') {
    return (
      <Routes>
        <Route path="/home" element={<LandingPage />} />
        <Route path="/donation" element={<DonationPage />} />
        <Route path="*" element={<LandingPage />} />
      </Routes>
    );
  } else if (userType === '0') {
    return (<Routes>
      <Route path="/employee" element={<EmployeePage />} />
      <Route path="/center" element={<CenterPage />} />
      <Route path="*" element={<EmployeePage />} />
    </Routes>
    );
  } else {
    return (<Routes>
      <Route path="/home" element={<LandingPage />} />
      <Route path="/signin" element={<SignIn />} />
      <Route path="/signup" element={<SignUp />} />
      <Route path="*" element={<LandingPage />} />
    </Routes>
    );
  }
};

export default BaseRoutes;
