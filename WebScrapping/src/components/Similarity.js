import React, { useState, Component } from "react";
import { Form, Col, Button, Table, Label, Container } from "react-bootstrap";
import Navbar from "./Navbar";
export default function Similarity() {
  const [values, setValues] = useState({
    url: "",
    url1: "",
  });
  const [responseData, setResponseData] = useState({
    similarityArray: [],
    ratioArray: [],
    keywordsUrl: [],
    keywordsUrl1: [],
    open: false,
  });

  const handleChange = (event) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value,
    });
  };
  const onSubmit = async (e) => {
    e.preventDefault();

    const requestOptions = {
      mode: "cors",
      credentials: "include",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({ url: values.url, urlOne: values.url1 }),
    };
    await fetch("/similarity", requestOptions)
      .then((response) => response.json())
      .then((data) =>
        setResponseData({
          similarityArray: data["matchList"],
          ratioArray: data["matchRatio"],
          keywordsUrl: data["keywordsUrl"],
          keywordsUrl1: data["keywordsUrl1"],
          open: true, 
        })
      );
    console.log("aaaaaa", responseData.similarityArray);

    // await fetch();
    console.log(values.url);
    console.log(values.url1);
  };
  return (
    <div>
      <Navbar className="container-fluid p-0 " />
    
      <Form onSubmit={onSubmit}>
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
              value={values.url}
              onChange={handleChange}
            />
            <Form.Control
              className="mb-2"
              id="inlineFormInput"
              name="url1"
              placeholder="Url Giriniz"
              type="text"
              value={values.url1}
              onChange={handleChange}
            />
          </Col>
          <Col xs="auto">
            <Button type="submit" className="mb-2">
              Anahtar Kelimeleri Bul
            </Button>
          </Col>

          {responseData.open && (
            <b class = "text-center font-weight-bold">Girilen Web Sitelerinin Benzerlik Skoru = %{responseData.ratioArray} </b>
          )}
        </Form.Row>
      </Form>

      {responseData.open && (
        <Container> 
        <b class = "text-center font-weight-bold">Girilen Sitelerin Benzer Kelimeleri  </b> 
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>#</th>
              <th>Kelime</th>
              <th>1. Sitedeki Frekans</th>
              <th>2. Sitedeki Frekans</th>
              <th>Benzerlik Oranı</th>
            </tr>
          </thead>

          {responseData.similarityArray.map((data, index) => (
            <tbody>
              <tr>
                <th>{index + 1}</th>
                <td>{data[0]}</td>
                <td>{data[1]}</td>
                <td>{data[2]}</td>
                <td>%{data[3]}</td>
              </tr>
            </tbody>
          ))}
        </Table>
        </Container>
        
      )}
      
      {responseData.open && (
        <Container>
        <b class = "text-center font-weight-bold">1. Sitenin Anahtar Kelimeleri  </b> 
        <Table striped bordered hover>
        
        <thead>
          <tr>
            <th>#</th>
            <th>Anahtar Kelime</th>
            <th>Frekans</th>
          </tr>
        </thead>

        {responseData.keywordsUrl.map((data, index) => (
          <tbody>
            <tr>
              <th>{index + 1}</th>
              <td>{data[0]}</td>
              <td>{data[1]}</td>
            </tr>
          </tbody>
        ))}
      </Table> </Container>
        
      )}
      
      {responseData.open && (
        <Container>
        <b class = "text-center font-weight-bold">2. Sitenin Anahtar Kelimeleri  </b> 
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>#</th>
              <th>Anahtar Kelime</th>
              <th>Frekans</th>
            </tr>
          </thead>

          {responseData.keywordsUrl1.map((data, index) => (
            <tbody>
              <tr>
                <th>{index + 1}</th>
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
