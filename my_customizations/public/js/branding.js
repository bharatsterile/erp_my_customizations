(function () {

	function apply_settings_branding() {
  	  // Change ERPNext Settings title
  	 		 document.querySelectorAll(".sidebar-item-label, .sidebar-item-label span").forEach(function (el) {
       			 if (el.textContent.trim() === "ERPNext Settings") {
          			  el.textContent = "BSAP Settings";
     			   }

      			  if (el.textContent.trim() === "ERPNext") {
       				     // Only change the small app label near ERPNext Settings
       				     const parent = el.closest(".sidebar-item");
        				    if (parent) {
        			     		   el.textContent = "BSAP";
         				   }
       				 }
   			 });


		// Settings page title
   		 $(".title-container .header-title").each(function () {
     		   if ($(this).text().trim() === "ERPNext Settings") {
       		     $(this).text("BSAP Settings");
      		  }
 		   });

  		  // Settings subtitle
   		 $(".title-container .header-subtitle").each(function () {
    		    if ($(this).text().trim() === "ERPNext") {
    		        $(this).text("BSAP");
  	   		   }
 		   });

  		  // Breadcrumb
  		  $(".worksapce-breadcrumb").each(function () {
     		   if ($(this).text().trim() === "ERPNext Settings") {
      		      $(this).text("BSAP Settings");
      		  }
  		  });
	}
   	 function apply_branding() {
      	  // Browser tab title
       		 document.title = "BSAP";

       		 // Replace ERPNext/Frappe logo
       		 const logo_url = "/assets/my_customizations/images/bsap-logo.jpg";

      		 // Replace Frappe logo
      		  const logo = document.getElementById("brand-logo");

      		  if (logo) {
         		   logo.src = logo_url;
         		   logo.removeAttribute("srcset");
          		  logo.alt = "BSAP";
     		   }  
		    // Settings branding
   	  	  apply_settings_branding();
	  	  customize_erpnext_settings();
 	   }

    function customize_erpnext_settings() {
		// Find ERPNext Settings desktop icon
		const item = document.querySelector(
			'a.desktop-icon[data-id="ERPNext Settings"]'
		);

		if (!item) return;
                
		// Change title
		const title = item.querySelector(".icon-title");
	        	
	      if (title && title.textContent.trim() !== "BSAP Settings") {
			title.textContent = "BSAP Settings";
			title.setAttribute("data-original-title", "BSAP Settings");
		}             
	    /*
		// Change icon
		const icon = item.querySelector("img.app-icon");
		if (icon) {
			icon.src = "/assets/my_customizations/images/bsap-logo.jpg";
			icon.alt = "BSAP Settings";
		}
		*/
	}


    // Initial load
    apply_branding();

    // Frappe route changes
    if (frappe.router) {
        frappe.router.on("change", function () {
            setTimeout(apply_branding, 100);
        });
    }

    // Frappe UI can recreate navbar elements
    const observer = new MutationObserver(function () {
        apply_branding();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
