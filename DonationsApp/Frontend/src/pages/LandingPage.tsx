import NavbarLayout from "../layouts";
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import './styles/LandingPage.css';


const LandingPage = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    centerMode: true,
    centerPadding: '0'
  };
  return (
    <NavbarLayout tab={"1"}>
      <div className="banner">
      <div className="container content-section">
        <h1 className="welcome-text">
          Welcome to Santa for a Day, a platform where you can spread happiness
          all year round!
        </h1>
      </div>
      </div>
      <Slider {...settings}>
      <div className="section-container">
      <div className="container content-section">
        <h2 className="section-title">
          WHO ARE WE?
        </h2>
        <div className="section-content">
        <p className="section-text">
          We are a non-profit organization dedicated to improving the lives
          of children who may not have access to the resources or support
          they need. We believe that every child deserves to feel loved,
          valued, and supported, and we strive to provide emotional support,
          quality time, and special gifts to these children.
        </p>
        <p className="section-text">
          Our organization provides events and activities that allow
          volunteers to spend time with children in need, engage in fun
          activities, and offer emotional support. We believe that these
          interactions can have a profound impact on a child's self-esteem,
          confidence, and overall well-being.
        </p>
        <p className="section-text">
          We also provide material gifts to children in need, including
          toys, games, clothing, and school supplies, with the goal of
          providing them with something special that they may not have had
          access to otherwise. And this is where you can help, by making a
          donation through our platform! Your donation can make a
          significant difference in their lives, and we are grateful for any
          support you can offer.
        </p>
        <p className="section-text">
          We recognize that children's lives can be improved in many ways,
          and we are committed to providing both emotional and material
          support to help make a difference in their lives. We invite you to
          join us in our mission to bring joy, hope, and positive change to
          the lives of these children.
        </p>
        </div>
      </div>
      </div>
      <div className="section-container">
      <div className="container content-section">
        <h2 className="section-title">
          HOW CAN YOU HELP US?
        </h2>
        <div className="section-content">
        <p className="section-text">
          Our organization is committed to making it easy and convenient for
          anyone to contribute and help make a positive difference in the
          lives of children in need. We believe that everyone has the power
          to give back to their community, and we are dedicated to providing
          an accessible platform to enable this.
        </p>
        <p className="section-text">
          Through our website, "Santa for a Day," you can donate a variety
          of items, such as toys, games, clothes, and school supplies. Once
          you have made your donation, one of our colleagues will collect it
          from the address you provide, making the process hassle-free and
          convenient.
        </p>
        <p className="section-text">
          We firmly believe that every child deserves to feel valued,
          supported, and loved, and we are passionate about our mission to
          make a positive impact in their lives. Whether you are an
          individual, family, or business, your contribution can make a
          significant difference to these children.
        </p>
        <p className="section-text">
          By donating to our organization, you can help bring happiness and
          hope to the lives      of these children. We invite you to join us in
      our efforts to create positive change and make a difference in
      your community.
    </p>
    </div>
  </div>
  </div>
  <div className="section-container">
  <div className="container content-section">
    <h2 className="section-title">
      TAKE A LOOK YOURSELF!
    </h2>
    <div className="section-content">
    <p className="section-text">
      Take a look at our activity section to see some of the incredible
      work we have done so far. We have organized toy drives,
      gift-giving events, and donation campaigns to ensure that every
      child receives something special. We also collaborate with local
      organizations to identify areas of need and provide assistance
      where it is needed most.
    </p>
    </div>
  </div>
  </div>
  </Slider>
  <div className="container content-section">
  <h1 className="closing-text">
        We thank you for your kindness and generosity, and we hope to continue
        making a positive impact together!
      </h1>
    </div>
</NavbarLayout>
);
};

export default LandingPage;