
var bowtieContentController = {

    initialize: function() {
        $('.js-st-instance').each(function(i, el) {
            var $el = $(el);
            var defaults = $el.data('sirtrevor-defaults');
            var conf = $el.data('sirtrevor-conf');
            var options;

            SirTrevor.setDefaults(defaults);
            options = _.extend({}, conf, {el: $el});

            new SirTrevor.Editor(options);
        });
    }

};

$(document).ready(function () {
    bowtieContentController.initialize();
});
