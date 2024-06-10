function adaptive_simpsons_rule_example
    a = 1.0;
    b = 3.0;
    tol = 1e-4;

    result = adaptive_simpsons_rule(@f, a, b, tol);
    disp(['Approximate integral: ', num2str(result)]);

    x = linspace(a, b, 400);
    y = arrayfun(@f, x);

    plot(x, y, 'DisplayName', 'f(x) = (100 / x^2) * sin(10 / x)');
    xlabel('x');
    ylabel('f(x)');
    title('Function plot for f(x) = (100 / x^2) * sin(10 / x)');
    legend show;
    grid on;
end

function y = f(x)
    y = (100 ./ x.^2) .* sin(10 ./ x);
end

function result = adaptive_simpsons_rule(f, a, b, tol, max_recursion_depth)
    if nargin < 5
        max_recursion_depth = 50;
    end

    result = recursive_asr(f, a, b, tol, simpsons_rule(f, a, b), max_recursion_depth);
end

function S = simpsons_rule(f, a, b)
    c = (a + b) / 2.0;
    h = b - a;
    S = (h / 6) * (f(a) + 4 * f(c) + f(b));
end

function result = recursive_asr(f, a, b, eps, whole, depth)
    c = (a + b) / 2.0;
    left = simpsons_rule(f, a, c);
    right = simpsons_rule(f, c, b);
    if depth <= 0 || abs(left + right - whole) <= 15 * eps
        result = left + right + (left + right - whole) / 15;
        return;
    end
    result = recursive_asr(f, a, c, eps/2, left, depth-1) + recursive_asr(f, c, b, eps/2, right, depth-1);
end

