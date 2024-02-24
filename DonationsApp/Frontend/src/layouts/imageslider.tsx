import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
//import image1 from "../assets/image1.jpg";
//import image2 from "../assets/image2.jpg";
//import image3 from "../assets/image3.jpg";

const ImageSlider = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  };

  return (
    <Slider {...settings}>
      <div>
        <img src="https://media.istockphoto.com/id/1172427455/photo/beautiful-sunset-over-the-tropical-sea.jpg?s=170667a&w=0&k=20&c=Ljvlgzgq8F1nVhc8YJM15CFgwu0ZsJvVrRnZPLtn9oU=" alt="image1" />
      </div>
      <div>
        <img src="https://earthsky.org/upl/2022/06/Christy-Mandeville_dramatic-sunset-with-child-silhouette_Indian-Shores-FL_2022-jun-08-800x450.jpg" alt="image2" />
      </div>
      <div>
        <img src="https://helpx.adobe.com/content/dam/help/en/lightroom-cc/how-to/enhance-sunset-photo/jcr_content/main-pars/before_and_after/image-after/enhance-sunset-photo_step-5after.jpg" alt="image3" />
      </div>
    </Slider>
  );
};

export default ImageSlider;
