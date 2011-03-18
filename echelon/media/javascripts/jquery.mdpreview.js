$(document).ready(function(){
  var object_field = $($(".livepreview").attr('id'));
  var converter = new Showdown.converter();

  var cached_input = object_field.val();
  var process = function process() {
      var pre_cache = object_field.val();
      $('.livepreview').html(converter.makeHtml(pre_cache));
      cached_input = pre_cache;
  };

  process();
  object_field.keydown(process);
  object_field.keyup(process);
});
