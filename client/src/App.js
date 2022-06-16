import React, { useState, useEffect } from 'react';
import Navbar from './components/navbar/Navbar';
import './styles/App.scss';

function App() {
	const [data, setData] = useState([{}]);

	useEffect(() => {
		fetch('/results')
			.then((res) => res.json())
			.then((data) => {
				setData(data);
				console.log(data);
			});
	}, []);

	return (
		<div className='App'>
			<Navbar />
			{typeof data.results === 'undefined' ? (
				<p>Loading...</p>
			) : (
				data.results.map((result, i) => {
					return <p key={i}>{result.name}</p>;
				})
			)}
		</div>
	);
}

export default App;
