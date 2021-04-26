import React, { Component } from "react";
import "./App.css";
import {BrowserRouter as Router , Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Keywords from "./components/Keywords";
import Frequency from "./components/Frequency";
import Similarity from "./components/Similarity";
import WebsiteIndexing from "./components/WebsiteIndexing";
import SemanticAnalysis from "./components/SemanticAnalysis";

class App extends Component {
 
  render() {
    return (
      <Router>
      <div>
        <Route exact path = "/" component = {Home}/>
        <Route path = "/hakkımızda" component = {About}/>
        <Route path = "/AnahtarKelime" component = {Keywords}/>
        <Route path = "/FrekansHesapla" component = {Frequency}/>
        <Route path = "/Benzerlik" component = {Similarity}/>
        <Route path = "/SiteIndeksleme" component = {WebsiteIndexing}/>
        <Route path = "/SemantikAnaliz" component = {SemanticAnalysis}/>
      </div>
      </Router>
      
    );
  }
}

export default App;
