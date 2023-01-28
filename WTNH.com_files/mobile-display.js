document.addEventListener("DOMContentLoaded", function () {
  const isMobile = () => window.matchMedia('(max-width: 512px)').matches;
  if (isMobile()) {
      // Remove Civic Science from sidebar in mobile view.
      const CsSidebarContainers = document.querySelectorAll('.civic-science-sidebar-container');
      CsSidebarContainers.forEach(sideContainer => {
          sideContainer.remove();
      });
  } else {
      // Remove Civic Science from content in desktop view.
      const CsContainers = document.querySelectorAll('.civic-science-container');
      CsContainers.forEach(container => {
          container.remove();
      });
  }
});
