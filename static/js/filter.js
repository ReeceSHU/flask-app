(() => {
  "use strict";
  // Add event listener to the department dropdown
  document.getElementById("department").addEventListener("change", function () {
    document.getElementById("filter-form").submit();
  });
})();