CV = (function() {

    var loadTemplate = function(templateId) {
        var el = document.getElementById(templateId);
        return el.textContent;
    };

    var renderSection = function(templateId, context) {
        var source = loadTemplate(templateId);
        var template = Handlebars.compile(source);
        return template(context);
    };

    var renderCV = function(containerQuery, cv) {
        var el;
        cv.email = new Handlebars.SafeString(cv.email);
        el = document.querySelector(containerQuery);
        el.innerHTML = renderSection('cv-html', cv);

        el = document.querySelector('title').textContent = 'CV for ' + cv.name;
        el = document.querySelector('.print-link');
        el.addEventListener('click', function(evt) {
            window.print();
            evt.preventDefault();
        });
    };

    return {
        render: renderCV
    };
}());

