const userShare = (user) => {
  if (navigator.share) {
    navigator
      .share({
        title: `PerQS - ${user}`,
        url: `http://localhost:8000/users/${user}`,
      })
      .catch(console.error);
  } else {
    navigator.clipboard
      .writeText(`http://localhost:8000/users/${user}`)
      .then(() => {
        alert("URLをコピーしました。");
      })
      .catch((error) => {
        console.error(error);
      });
  }
};
