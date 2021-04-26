import React, { Fragment } from "react";
import Card from "./Card/Card.js";
import frekansPhoto from "../assets/frekans.jpg";
import anahtarKelime from "../assets/anahtarKelime.jpg";
import benzerlik from "../assets/benzerlik.jpg";
import Indeks from "../assets/indexing.jpg";
import semantikAnaliz from "../assets/semantikAnaliz.png";
import Navbar from "./Navbar";
import {Row , Col} from "react-bootstrap";


export default function Home() {

  const cardObj = [
    {
      id: 1,
      image: frekansPhoto,
      header: "Frekans Hesaplama",
      description:
        "Açılan sayfada verilen boşluğa girmiş olduğunuz site içerisindeki kelimelerin frekansını bulabilirsiniz",
      font: "fas fa-wave-square",
      link : "/FrekansHesapla",
    },
    {
      id: 2,
      image: anahtarKelime,
      header: "Anahtar Kelimeleri Bulma",
      description:
        "Açılan sayfada verilen boşluğa girmiş olduğunuz site içerisindeki anahtar kelimeleri bulabilirsiniz",
      font: "fas fa-key",
      link : "/AnahtarKelime",
    },
    {
      id: 3,
      image: benzerlik,
      header: "Benzerlik Oranı Hesaplama",
      description:
      " Açılan sayfada verilen iki boşluğa girmiş olduğunuz siteler arasındaki benzerlik oranını bulabilirsiniz",
      font: "fas fa-hand-paper",
      link : "/Benzerlik",
    },
    {
      id: 4,
      image: Indeks,
      header: "Site Indexleme ve Sıralama",
      description:
        "Açılan sayfada verilen boşluğa girmiş olduğunuz siteler içerisindeki benzerlik bulabilirsiniz",
      font: "fas fa-sort-amount-down-alt",
      link : "/SiteIndeksleme",
    },
    {
      id: 5,
      image: semantikAnaliz,
      header: "Semantik Analiz",
      description:
        " Açılan sayfada verilen boşluğa girmiş olduğunuz site içerisindeki anahtar kelimeleri bulabilirsiniz",
      font: "fas fa-chart-line",
      link : "/SemantikAnaliz",
    },
  ];

  return (
    <Fragment>
    <Navbar/>
    <hr/>
    <Row>
    {cardObj.map((el) => (
        <Col key = {el.id}>
      
        <Card
          id={el.id}
          image={el.image}
          header={el.header}
          description={el.description}
          font={el.font}
          link = {el.link}
        />
          
        </Col>
      ))}
    </Row>
      
    </Fragment>
    
  );
}
