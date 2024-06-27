import TextAnim from "./TextAnim";
// import Input from "./components/Input";
import City from "./components/City";
import image from './assets/artist.png';
import { useState } from "react";


export default function Hero() {

  const [locations, setLocations] = useState([{
    id: 0,
    value: ''
  }]);

  const transformArray = (items: {
    id: number;
    value: string;
  }[]) => {
    const locations = items.map(item => item.value);
    return { locations };
  };

  const addCity = (city: string) => {
    setLocations((prevItems) => {
      const lastItem = prevItems[prevItems.length - 1];
      if (lastItem.value === '') {
        return prevItems.map((item, index) =>
          index === prevItems.length - 1 ? { ...item, value: city } : item
        );
      } else {
        return [...prevItems, { id: prevItems.length + 1, value: city }];
      }
    });
  }

  const handleAddLocation = () => {
    setLocations((locations) => [
      ...locations,
      { id: locations.length + 1, value: '' },
    ]);
  };

  const handleChange = (id: number, newValue: string) => {
    setLocations((prevInputs) =>
      prevInputs.map((input) =>
        input.id === id ? { ...input, value: newValue } : input
      )
    );
  };

  const handleDeleteInput = (id: number) => {
    setLocations((prevInputs) => prevInputs.filter((input) => input.id !== id));
  };

  const submit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('/submit-form', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(transformArray(locations))
      });
      const result = await response.json();
      if (result.status === "ok") {
        window.location.href = "/auth/spotify";
      } else {
        throw new Error("didn't work");
      }
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <section className="max-w-[1024px] flex flex-col items-center">
      <div className=" flex flex-col items-center">
        <TextAnim />
        <div className="text-2xl my-20 text-justify">
          Explore Your Local Sound: Discover emerging artists and hidden musical gems in your area with our platform. Uncover a diverse range of genres and support talented musicians right in your neighborhood. Whether you're into indie rock, hip-hop, folk, or electronic beats, find your next favorite song from local artists on our curated platform.
        </div>
      </div>
      {/* <Input /> */}


      <div className='relative w-full'>
      <form onSubmit={submit} >
        {locations.map((input, index) => (
          
          <div key={input.id} className='flex flex-col'>
            
            <div className='border-b-2 flex space-between'>
              <input
                className='text-3xl bg-transparent border-0 outline-none flex-grow'
                type="text"
                value={input.value}
                onChange={(e) => handleChange(input.id, e.target.value)}
                placeholder={`Enter location`}
                required
              />
              {index == 0 && (
                <button type='button' onClick={handleAddLocation} className='bg-transparent pl-1 pr-0 pb-1 border-0'>
                  <svg xmlns="http://www.w3.org/2000/svg" width="30px" height="30px" viewBox="0 0 60 60" fill="none">
                    <path d="M30 20V30M30 30V40M30 30H40M30 30H20M55 30C55 43.8071 43.8071 55 30 55C16.1929 55 5 43.8071 5 30C5 16.1929 16.1929 5 30 5C43.8071 5 55 16.1929 55 30Z" stroke="white" stroke-width="5" stroke-linecap="round"/>
                  </svg>
                </button>
              )}
              {index > 0 && (
                <button type="button" onClick={() => handleDeleteInput(input.id)} className='bg-transparent pl-1 pr-0 pb-1 border-0'>
                  <svg xmlns="http://www.w3.org/2000/svg" width="30px" height="30px" viewBox="0 0 60 60" fill="none">
                    <path d="M40 30H20M55 30C55 43.8071 43.8071 55 30 55C16.1929 55 5 43.8071 5 30C5 16.1929 16.1929 5 30 5C43.8071 5 55 16.1929 55 30Z" stroke="white" stroke-width="5" stroke-linecap="round"/>
                  </svg>
                </button>
              )}
            </div>
            
          </div>
        ))}
        <div className='text-gray-300 text-left mt-4'>
          E.g. Champaign <br/> Add multiple locations by clicking on the plus button. Locations can be added from below as well.
        </div>
        <button type="submit" className='px-5 bg-accent rounded-3xl text-2xl font-bold absolute right-0 mt-8'>Next</button>
      </form>
    </div>



    <div className="mt-60 relative">
      <img src={image} alt="Local artist playing music" className='absolute r-0 z-[-1]' />
      <h1 className='text-7xl font-bold text-left'>Recommended Locations</h1>
      <div className='mx-20'>
        <div className='flex justify-around mt-16'>
          <City cityName="Champaign" color="#BE397A" addCity={addCity}/>
          <City cityName="Chicago" color="#164486" addCity={addCity}/>
          <City cityName="Atlanta" color="#4F3837" addCity={addCity}/>
        </div>
        <div className='flex justify-around mt-12'>
          <City cityName="Austin" color="#962529" addCity={addCity}/>
          <City cityName="Seattle" color="#2A8280" addCity={addCity}/>
          <City cityName="Los Angeles" color="#B99A29" addCity={addCity}/>
        </div>
        <div className='flex justify-around mt-12'>
          <City cityName="San Francisco" color="#C25F1F" addCity={addCity}/>
          <City cityName="Miami" color="#4DA4C6" addCity={addCity}/>
          <City cityName="Houston" color="#6B8E23" addCity={addCity}/>
          
        </div>
      </div>
    </div>

    </section>     
  )
}