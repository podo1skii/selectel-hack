import React, { Component } from "react";
import "./App.css";
import Header from "./header/header";
import StartScreen from "./start-screen/start-screen";
import OneWordGame from "./one-word-game/one-word-game";
import EffortAndPainGame from "./effort-and-pain-game/effort-and-pain-game";
import ThreeLittlePigsGame from "./three-little-pigs-game/three-little-pigs-game";
import FinalPage from "./final-page/final-page";

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			appStatus: "final" //'start', 'OW', 'EAP', 'TLP', 'final'
		};
	}

	render() {
		return (
			<>
				<Header></Header>
				{this.state.appStatus === "start" && <StartScreen></StartScreen>}
				{this.state.appStatus === "OW" && <OneWordGame />}
				{this.state.appStatus === "EAP" && <EffortAndPainGame />}
				{this.state.appStatus === "TLP" && <ThreeLittlePigsGame />}
				{this.state.appStatus === "final" && <FinalPage/>}
			</>
		);
	}
}

export default App;
