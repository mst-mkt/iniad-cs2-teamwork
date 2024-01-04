const logout = () => {
  const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const csrftoken = getCookie("csrftoken");

  confirm("ログアウトしますか？") &&
    fetch("/logout/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": csrftoken,
      },
    })
      .then((response) => {
        if (response.ok) {
          location.href = "/login";
        } else {
          alert("ログアウトに失敗しました。");
        }
      })
      .catch((error) => {
        console.error(error);
      });
};
