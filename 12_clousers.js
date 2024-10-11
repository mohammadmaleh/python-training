const parentFunction = (name, coins) => {
  // let coins = 3
  const playGame = () => {
    coins -= 1;
    if (coins > 1) {
      console.log(name + " have " + coins + " coins left");
    } else if (coins == 1) {
      console.log(name + " have " + coins + " coin left");
    } else {
      console.log(name + " have no coins left");
    }
  };

  return playGame;
};

const tommy = parentFunction("mohammad", 3);
const jenny = parentFunction("jenny", 5);
tommy();
tommy();
jenny();
jenny();
