$(function() {
    // For rendering markdown preview in the admin
    var markdown_preview = $('#markdown_preview');
    var content = $('#id_content');
    var converter = new Showdown.converter();
    
    var cached_input = content.val();
    
    var process = function() {
        if (content.val() == cached_input) {
            return;
        }
        var pre_cache = content.val();
        markdown_preview.html(converter.makeHtml(pre_cache));
        cached_input = pre_cache;
    };
    
    // add event for keyup and focus
    content.keydown(process);
    content.keyup(process);
    
    // clear the search box
    var search_box = $('#search');
    
    search_box.focus(function() {
       search_box.val('') ;
    });

    // drag and drop admin interface
    var list = $('#sortable');
    var save_sort = $('#sortable_button');

    list.sortable();
    list.disableSelection();

    save_sort.click(function() {
        list.children().each(function(i) {
          $(this).children('input').val(i);
        });
    });
});
