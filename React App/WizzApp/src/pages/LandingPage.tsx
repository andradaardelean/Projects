import Offers from '~/components/Offers';
import SearchForm from '~/components/SearchForm';
import NavbarLayout from '~/layouts';

const LandingPage = () => {
  return (
    <NavbarLayout>
      <SearchForm />
      <Offers />
    </NavbarLayout>
  );
};

export default LandingPage;
