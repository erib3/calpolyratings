$(document).ready(function() {  
  $('a[href="'+ this.location.pathname + '"]').parents('div,li').addClass('active');
});