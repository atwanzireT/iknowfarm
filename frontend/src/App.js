import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/register/login';
import Forgot from './components/register/Forgot';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/login' element = {<Login/>} />
        <Route path='/forgotpassword' element = {<Forgot/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
