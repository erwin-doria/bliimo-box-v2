const pathConfig = () => {
  const menu = $('#menus');
  const fab =
    ' <div class="fab child" data-subitem="5" id="fab-dl-events"> <a href="javascript:void(0)" onclick="downloadEvents()" class="text-light"> <i class="fas fa-calendar-check menu-icon"></i> </a> </div>';

  if (window.location.pathname == '/events') {
    menu.append(fab);
    $('#bg-main').hide();
    $('#item-dl-events').show();
  } else {
    $('#item-dl-events').hide();
    $('#fab-dl-events').remove();
  }

  if (window.location.pathname == '/login') {
    $('#navbar').hide();
    $('#menus').hide();
  } else {
  }
};

const setActive = () => {
  const items = $('.nav-item');
  items.each((i, item) => {
    if (
      $(item)
        .find('a')
        .attr('href') == window.location.pathname
    ) {
      $(item).addClass('active');
    }
  });
};

$('#loginForm').on('submit', function(e) {
  e.preventDefault();
  const loginBtn = $('#btnLogin');
  loginBtn.text('Please wait');
  loginBtn.prop('disabled', true);
  login({ usernameOrEmail: $('#user').val(), password: $('#pass').val() });
  setTimeout(() => {
    loginBtn.text('Login');
    loginBtn.prop('disabled', false);
  }, 1500);
});

const setMenu = () => {
  setTimeout(() => {
    $('#menus').hide();
  }, 5000);

  $('html').click(function(e) {
    if (
      window.location.pathname != '/login' &&
      $(e.target).hasClass('card-body') != true &&
      $(e.target).attr('id') != 'download-btn' &&
      $(e.target)[0].nodeName == 'DIV' &&
      $(window).width() <= 1000
    ) {
      $('#menus').show();
      setTimeout(() => {
        if ($('.backdrop').css('display') == 'none') {
          $('#menus').hide();
        }
      }, 5000);
    }
  });
};

$(function() {
  $('.fab,.backdrop').click(function() {
    if ($('.backdrop').is(':visible')) {
      $('.backdrop').fadeOut(125);
      $('.fab.child')
        .stop()
        .animate(
          {
            bottom: $('#masterfab').css('bottom'),
            opacity: 0
          },
          125,
          function() {
            $(this).hide();
          }
        );
    } else {
      $('.backdrop').fadeIn(125);
      $('.fab.child').each(function() {
        $(this)
          .stop()
          .show()
          .animate(
            {
              bottom:
                parseInt($('#masterfab').css('bottom')) +
                parseInt($('#masterfab').outerHeight()) +
                70 * $(this).data('subitem') -
                $('.fab.child').outerHeight() +
                'px',
              opacity: 1
            },
            125
          );
      });
    }
  });
});

$(window).on('load', function() {
  setMenu();
  $('.ellipsis').ellipsis();
  setTimeout(function() {
    $('.se-pre-con').hide();
  }, 1500);
});

$(window).resize(function() {
  $('.ellipsis').ellipsis();
});
