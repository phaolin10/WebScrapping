import React from 'react'
import {
    Image,
    Button,
    Col,
  } from "react-bootstrap";
import { Link } from "react-router-dom";


export default function Card(props) {
    return (
     
        <Col>
        
        <Button
        className="container-right btn btn-dark btn-block mb-2 "
        
      size="sm"
      >
      <Link to ={props.link}> 
        <Image src={props.image} roundedCircle />
        <h2>
         {props.header} <i class={props.font}></i>{" "}
        </h2>
        <p>
          {props.description}
        </p>
        </Link>
      </Button>
      </Col>
      
    )
}
