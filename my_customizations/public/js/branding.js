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
		const title = item.querySelector(".icon-title");	        	
	        if (title && title.textContent.trim() !== "BSAP Settings") {
			title.textContent = "BSAP Settings";
			title.setAttribute("data-original-title", "BSAP Settings");
		}     
                // Find Frappe Insights desktop icon
                const itemI = document.querySelector(
                        'a.desktop-icon[data-id="Frappe Insights"]'
                );
                if (!itemI) return;
                const title_I = itemI.querySelector(".icon-title");
                if (title_I && title_I.textContent.trim() !== "BSAP Insights") {
                        title_I.textContent = "BSAP Insights";
                        title_I.setAttribute("data-original-title", "BSAP Insights");
		}
				
				
		// Find Frappe HR desktop icon
                const itemHR = document.querySelector(
                        'a.desktop-icon[data-id="Frappe HR"]'
                );
                if (!itemHR) return;
                const title_HR = itemHR.querySelector(".icon-title");
                if (title_HR && title_HR.textContent.trim() !== "BSAP HR") {
                        title_HR.textContent = "BSAP HR";
                        title_HR.setAttribute("data-original-title", "BSAP HR");
                }

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
