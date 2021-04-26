import React, { Component, useState, useEffect } from "react";
import { Form, Col, Button, Table, Container } from "react-bootstrap";
import Navbar from "./Navbar";

export default class Frequency extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
      frequenciesArray: [],
      open: false,
    };

     this.handleChange = this.handleChange.bind(this);
     this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
  }

  SendFetch = async () => {
    console.log(this.state.value);
    const requestOptions = {
      mode : 'cors',
      credentials : 'include',
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'Accept' : 'application/json',
       },
      body: JSON.stringify({ url : this.state.value }),
  };

    await fetch("/frequency",requestOptions)
    .then((response) => response.json())
    .then((data) => this.setState({ frequenciesArray: data, open: true }));
    console.log("asdasf",this.state.frequenciesArray)
      
  }

  render() {
    return (
      <div>
        <Navbar className="container-fluid p-0 " />

        <Form onSubmit={this.handleSubmit}>
          <Form.Row className="align-items-center">
            <Col xs="auto">
              <Form.Label htmlFor="url" name="url" type="text" srOnly>
                Hesaplanmasını istediğiniz
              </Form.Label>
              <Form.Control
                className="mb-2"
                id="inlineFormInput"
                name="url"
                placeholder="Url Giriniz"
                type="text"
                value={this.state.value}
                onChange={this.handleChange}
              />
            </Col>
            <Col xs="auto">
              <Button type="submit" className="mb-2" onClick={this.SendFetch}>
                Frekans Hesapla
              </Button>
            </Col>
          </Form.Row>
        </Form>

        {this.state.open && (
          <Container>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>#</th>
                <th>Kelime</th>
                <th>Frekans</th>
              </tr>
            </thead>

            {this.state.frequenciesArray.map((data, index) => (
              <tbody>
                <tr>
                  <td>{index + 1}</td>
                  <td>{data[0]}</td>
                  <td>{data[1]}</td>
                </tr>
              </tbody>
            ))}
          </Table>
          </Container>
          
        )}
        
      </div>
    );
  }
}
