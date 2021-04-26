import React, { useState, Component } from "react";
import { Form, Col, Button, Table, Label, Container } from "react-bootstrap";
import Navbar from "./Navbar";

export default function SemanticAnalysis() {
  const [values, setValues] = useState({
    url: "",
  });
  const [responseData, setResponseData] = useState({
    keywordsUrl: [],
    inWebsiteSemanticWords: [],
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
      body: JSON.stringify({ url: values.url }),
    };
    await fetch("/semanticAnalysis", requestOptions)
      .then((response) => response.json())
      .then((data) =>
        setResponseData({
          inWebsiteSemanticWords : data,
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
          </Col>
          <Col xs="auto">
            <Button type="submit" className="mb-2">
              Semantik Analiz Yap
            </Button>
          </Col>
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
              <th>Eş Anlamlısı</th>
            </tr>
          </thead>

          {responseData.inWebsiteSemanticWords.map((data, index) => (
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
