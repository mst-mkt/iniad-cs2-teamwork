const openModal = () => {
  const modalElement = document.getElementsByClassName("modal")[0];
  modalElement.classList.add("is-active");
};

const closeModal = () => {
  const modalElement = document.getElementsByClassName("modal")[0];
  modalElement.classList.remove("is-active");
};
