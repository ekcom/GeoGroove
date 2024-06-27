// import { useState } from 'react';

// export default function Input(locations: [{id: number, value: string}], setLocations: React.Dispatch<React.SetStateAction<[{id: number, value: string}]>>) {

  

//   const handleAddLocation = () => {
//     setLocations((locations) => [
//       ...locations,
//       { id: locations.length + 1, value: '' },
//     ]);
//   };

//   const handleChange = (id: number, newValue: string) => {
//     setLocations((prevInputs) =>
//       prevInputs.map((input) =>
//         input.id === id ? { ...input, value: newValue } : input
//       )
//     );
//   };

//   const handleDeleteInput = (id: number) => {
//     setLocations((prevInputs) => prevInputs.filter((input) => input.id !== id));
//   };

//   const submit = async () => {
//     try {
//       const response = await fetch('/submit-form', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(locations)
//       });
//       const result = await response.json();
//       console.log('Form submitted successfully:', result);
//     } catch (error) {
//       console.error('Error submitting form:', error);
//     }
//   };

//   return (
//     <div className='relative w-full'>
//       <form onSubmit={submit} >
//         {locations.map((input, index) => (
          
//           <div key={input.id} className='flex flex-col'>
            
//             <div className='border-b-2 flex space-between'>
//               <input
//                 className='text-3xl bg-transparent border-0 outline-none flex-grow'
//                 type="text"
//                 value={input.value}
//                 onChange={(e) => handleChange(input.id, e.target.value)}
//                 placeholder={`Enter location`}
//                 required
//               />
//               {index == 0 && (
//                 <button type='button' onClick={handleAddLocation} className='bg-transparent pl-1 pr-0 pb-1 border-0'>
//                   <svg xmlns="http://www.w3.org/2000/svg" width="30px" height="30px" viewBox="0 0 60 60" fill="none">
//                     <path d="M30 20V30M30 30V40M30 30H40M30 30H20M55 30C55 43.8071 43.8071 55 30 55C16.1929 55 5 43.8071 5 30C5 16.1929 16.1929 5 30 5C43.8071 5 55 16.1929 55 30Z" stroke="white" stroke-width="5" stroke-linecap="round"/>
//                   </svg>
//                 </button>
//               )}
//               {index > 0 && (
//                 <button type="button" onClick={() => handleDeleteInput(input.id)} className='bg-transparent pl-1 pr-0 pb-1 border-0'>
//                   <svg xmlns="http://www.w3.org/2000/svg" width="30px" height="30px" viewBox="0 0 60 60" fill="none">
//                     <path d="M40 30H20M55 30C55 43.8071 43.8071 55 30 55C16.1929 55 5 43.8071 5 30C5 16.1929 16.1929 5 30 5C43.8071 5 55 16.1929 55 30Z" stroke="white" stroke-width="5" stroke-linecap="round"/>
//                   </svg>
//                 </button>
//               )}
//             </div>
            
//           </div>
//         ))}
//         <div className='text-gray-300 text-left mt-4'>
//           E.g. Champaign <br/> Add multiple locations by clicking on the plus button. Locations can be added from below as well.
//         </div>
//         <button type="submit" className='px-5 bg-accent rounded-3xl text-2xl font-bold absolute right-0 mt-8'>Next</button>
//       </form>
//     </div>
//   );
// }
  