import React from "react";
import PropTypes from "prop-types";
import { Navbar, Nav } from "react-bootstrap";


function NavbarTop(props) {
  return (
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Navbar.Brand href="/">Web Indeksleme Projesi</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />

      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="mr-auto">
          <Nav.Link href="/">Anasayfa</Nav.Link>
          <Nav.Link href="/icerik">Proje Icerigi</Nav.Link>
        </Nav>

        <Nav>
          <Nav.Link href="/iletisim">Iletisim</Nav.Link>
          <Nav.Link href="/hakkımızda">Hakkımızda</Nav.Link>
          <Nav.Link href="/instagram">
            <i class="fab fa-instagram"></i>
          </Nav.Link>
          <Nav.Link href="/twitter">
            <i class="fab fa-twitter"></i>
          </Nav.Link>
          <Nav.Link href="/youtube">
            <i class="fab fa-youtube"></i>
          </Nav.Link>
          <Nav.Link href="/facebook">
            <i class="fab fa-facebook"></i>
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

Navbar.propTypes = {
  title: PropTypes.string.isRequired,
};
Navbar.defaultProps = {
  title: "Çalışanlar",
};
export default NavbarTop;
